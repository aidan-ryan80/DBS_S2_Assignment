CREATE DATABASE SkiHotelDB;
USE SkiHotelDB;

-- Creating the tables in SkiHotelDB Database
CREATE TABLE IF NOT EXISTS hotel (
    hotelID INT PRIMARY KEY AUTO_INCREMENT,
    address VARCHAR(100) NOT NULL, 
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS customer (
    customerID INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL, 
    phoneNumber VARCHAR(15) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    age VARCHAR(50) DEFAULT NULL,
    address VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS paymentInfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customerID INT,
    billingAddress VARCHAR(100) NOT NULL,
    cardHolderName VARCHAR(100) NOT NULL,
    expirationDate DATE NOT NULL,
    cardIssuer VARCHAR(20) NOT NULL,
    cardNumber VARCHAR(19) NOT NULL UNIQUE,
    FOREIGN KEY (customerID) REFERENCES customer(customerID)
);

CREATE TABLE IF NOT EXISTS room (
    roomNumber SMALLINT(3) NOT NULL PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    type ENUM('single', 'double', 'triple', 'quadruple') NOT NULL,
    availability ENUM('available', 'unavailable') NOT NULL,
    floor TINYINT GENERATED ALWAYS AS (roomNumber DIV 100) STORED
);

CREATE TABLE IF NOT EXISTS skiResort (
    resortID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    size FLOAT(4, 2) CHECK (size > 0),
    location VARCHAR(255),
    difficultyLevel ENUM('Beginner', 'Intermediate', 'Advanced', 'Expert'),
    skiLiftsCount SMALLINT CHECK (skiLiftsCount > 0),
    slopesCount SMALLINT CHECK (slopesCount > 0)
);

CREATE TABLE IF NOT EXISTS businessHour (
    id INT AUTO_INCREMENT PRIMARY KEY,
    resortID INT,
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'),
    open_time TIME,
    close_time TIME,
    FOREIGN KEY (resortID) REFERENCES skiResort(resortID)
);

CREATE TABLE IF NOT EXISTS skiPass (
    skiPassID INT AUTO_INCREMENT PRIMARY KEY,
    resortID INT,
    passType ENUM('Day Pass', '2 Day Pass', '3 Day Pass', '4 Day Pass', '5 Day Pass', '6 Day Pass', '7 Day Pass'),
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    FOREIGN KEY(resortID) REFERENCES skiResort(resortID)
);

CREATE TABLE IF NOT EXISTS package (
    packageID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    roomID SMALLINT(3),
    skiPassID INT,
    FOREIGN KEY(roomID) REFERENCES room(roomNumber),
    FOREIGN KEY(skiPassID) REFERENCES skiPass(skiPassID)
);

CREATE TABLE IF NOT EXISTS transport (
    transportID INT AUTO_INCREMENT PRIMARY KEY,
    resortID INT,
    type ENUM('shuttle', 'train', 'helicopter', 'snowmobile') NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    timetable TEXT,
    FOREIGN KEY(resortID) REFERENCES skiResort(resortID)
);

CREATE TABLE IF NOT EXISTS packageTransport (
    packageID INT,
    transportID INT,
    PRIMARY KEY (packageID, transportID),
    FOREIGN KEY (packageID) REFERENCES package(packageID) ON DELETE CASCADE,
    FOREIGN KEY (transportID) REFERENCES transport(transportID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS reservation (
    reservationID INT PRIMARY KEY AUTO_INCREMENT,
    status ENUM('pending', 'confirmed', 'cancelled', 'completed', 'no_show', 'expired', 'failed') NOT NULL,
    paymentStatus ENUM('payed', 'unpayed', 'failed') NOT NULL,
    checkInDate DATE NOT NULL,
    checkOutDate DATE NOT NULL,
    totalCost DECIMAL(10, 2) NOT NULL CHECK (totalCost > 0),
    hotelID INT UNIQUE,
    customerID INT,
    roomID SMALLINT(3),
    FOREIGN KEY (hotelID) REFERENCES hotel(hotelID),
    FOREIGN KEY (customerID) REFERENCES customer(customerID),
    FOREIGN KEY (roomID) REFERENCES room(roomNumber)
);

-- Could be used for the the reservation table:
-- startDate DATETIME NOT NULL,
-- endDate DATETIME NOT NULL,
-- validityPeriod INT AS (TIMESTAMPDIFF(DAY, startDate, endDate)) STORED,
-- CHECK (validityPeriod > 0),