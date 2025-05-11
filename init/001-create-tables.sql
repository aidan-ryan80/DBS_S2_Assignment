USE SkiHotelDB;

-- Creating the tables in SkiHotelDB Database
CREATE TABLE IF NOT EXISTS Hotel (
    hotelID INT PRIMARY KEY DEFAULT 1,
    address VARCHAR(100) NOT NULL, 
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Customers (
    customerID INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL, 
    phoneNumber VARCHAR(15) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    age VARCHAR(50) DEFAULT NULL,
    address VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS PaymentInfos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customerID INT,
    billingAddress VARCHAR(100) NOT NULL,
    cardHolderName VARCHAR(100) NOT NULL,
    expirationDate DATE NOT NULL,
    cardIssuer VARCHAR(20) NOT NULL,
    cardNumber VARCHAR(19) NOT NULL UNIQUE,
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);

CREATE TABLE IF NOT EXISTS Rooms (
    roomNumber SMALLINT(3) NOT NULL PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    type ENUM('single', 'double', 'triple', 'quadruple') NOT NULL,
    availability ENUM('available', 'unavailable') NOT NULL,
    floor TINYINT GENERATED ALWAYS AS (roomNumber DIV 100) STORED
);

CREATE TABLE IF NOT EXISTS SkiResorts (
    resortID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    size FLOAT(4, 2) CHECK (size > 0),
    location VARCHAR(255),
    difficultyLevel ENUM('Beginner', 'Intermediate', 'Advanced', 'Expert'),
    skiLiftsCount SMALLINT CHECK (skiLiftsCount > 0),
    slopesCount SMALLINT CHECK (slopesCount > 0),
    businessHours TEXT
);

CREATE TABLE IF NOT EXISTS BusinessHours (
    id INT AUTO_INCREMENT PRIMARY KEY,
    resortID INT,
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'),
    open_time TIME,
    close_time TIME,
    FOREIGN KEY (resortID) REFERENCES SkiResorts(resortID)
);

CREATE TABLE IF NOT EXISTS SkiPasses (
    skiPassID INT AUTO_INCREMENT PRIMARY KEY,
    resortID INT,
    passType ENUM('Day Pass', '2 Day Pass', '3 Day Pass', '4 Day Pass', '5 Day Pass', '6 Day Pass', '7 Day Pass'),
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    FOREIGN KEY(resortID) REFERENCES SkiResorts(resortID)
);

CREATE TABLE IF NOT EXISTS Packages (
    packageID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) CHECK (price > 0),
    roomID SMALLINT(3),
    skiPassID INT,
    FOREIGN KEY(roomID) REFERENCES Rooms(roomNumber),
    FOREIGN KEY(skiPassID) REFERENCES SkiPasses(skiPassID)
);

CREATE TABLE IF NOT EXISTS Transports (
    transportID INT AUTO_INCREMENT PRIMARY KEY,
    resortID INT,
    type ENUM('shuttle', 'train', 'helicopter', 'snowmobile') NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    timetable TEXT,
    FOREIGN KEY(resortID) REFERENCES SkiResorts(resortID)
);

CREATE TABLE IF NOT EXISTS PackagesTransports (
    packageID INT,
    transportID INT,
    PRIMARY KEY (packageID, transportID),
    FOREIGN KEY (packageID) REFERENCES Packages(packageID) ON DELETE CASCADE,
    FOREIGN KEY (transportID) REFERENCES Transports(transportID) ON DELETE CASCADE
);

DELIMITER $$

CREATE TRIGGER trg_set_package_price
BEFORE INSERT ON Packages
FOR EACH ROW
BEGIN
    DECLARE skiPass_price DECIMAL(10,2);
    SELECT price INTO skiPass_price FROM SkiPasses WHERE skiPassID = NEW.skiPassID;
    SET NEW.price = skiPass_price;
END$$

CREATE TRIGGER trg_add_transport_price
AFTER INSERT ON PackagesTransports
FOR EACH ROW
BEGIN
    UPDATE Packages
    SET price = price + (
        SELECT price
        FROM Transports
        WHERE transportID = NEW.transportID
    )
    WHERE packageID = NEW.packageID;
END$$

CREATE TRIGGER trg_subtract_transport_price
AFTER DELETE ON PackagesTransports
FOR EACH ROW
BEGIN
    UPDATE Packages
    SET price = price - (
        SELECT price
        FROM Transports
        WHERE transportID = OLD.transportID
    )
    WHERE packageID = OLD.packageID;
END$$

DELIMITER ;

CREATE TABLE IF NOT EXISTS Reservations (
    reservationID INT PRIMARY KEY AUTO_INCREMENT,
    status ENUM('pending', 'confirmed', 'cancelled', 'completed', 'no_show') NOT NULL,
    paymentStatus ENUM('payed', 'unpayed', 'failed') NOT NULL,
    checkInDate DATE NOT NULL,
    checkOutDate DATE NOT NULL,
    totalCost DECIMAL(10, 2) CHECK (totalCost > 0),
    hotelID INT,
    customerID INT,
    packageID INT DEFAULT NULL,
    roomID SMALLINT(3),
    FOREIGN KEY (hotelID) REFERENCES Hotel(hotelID),
    FOREIGN KEY (customerID) REFERENCES Customers(customerID),
    FOREIGN KEY (packageID) REFERENCES Packages(packageID),
    FOREIGN KEY (roomID) REFERENCES Rooms(roomNumber)
);

DELIMITER $$

CREATE TRIGGER set_reservation_price
BEFORE INSERT ON Reservations
FOR EACH ROW
BEGIN
    DECLARE room_price DECIMAL(10, 2);
    DECLARE package_price DECIMAL(10, 2);

    -- Fetching room price from room table based on roomID
    SELECT price INTO room_price
    FROM Rooms
    WHERE roomNumber = NEW.roomID;

    IF NEW.packageID IS NOT NULL THEN
        SELECT price INTO package_price
        FROM Packages
        WHERE packageID = NEW.packageID;

        SET NEW.totalCost = package_price + room_price * DATEDIFF(NEW.checkOutDate, NEW.checkInDate);
    ELSE
        SET NEW.totalCost = room_price * DATEDIFF(NEW.checkOutDate, NEW.checkInDate);
    END IF;

END$$

DELIMITER ;