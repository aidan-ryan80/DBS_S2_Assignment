# Module Imports
import mariadb
import sys

# Connect to MariaDB
try:
    conn = mariadb.connect(
        user="root",
        password="rootpass",
        host="localhost",
        port=3306,
        database="HospitalDB"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Getting a Cursor
cur = conn.cursor()

cur.execute("""
CREATE TABLE hotel (
    hotelID INT PRIMARY KEY AUTO_INCREMENT,
    address VARCHAR(100) NOT NULL, 
    name VARCHAR(100) NOT NULL
);
""")

# ? From email, name, age, address, and phoneNumber what should be NOT NULL?
cur.execute("""
CREATE TABLE customer (
    customerID INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL, 
    phoneNumber VARCHAR(15) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    age VARCHAR(50) NOT NULL,
    address VARCHAR(100) NOT NULL
);
""")

# Apparently for payment only certified payment processors should store credit card numbers, CVV codes, Expiration dates, and cardholder names. 
# Instead token or ID's are stored and referenced. For now I will include payment information for the customer, and each reservation
cur.execute("""
CREATE TABLE paymentInfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customerID INT,
    billingAddress VARCHAR(100) NOT NULL,
    cardHolderName VARCHAR(100) NOT NULL,
    expirationDate DATE NOT NULL,
    cardIssuer VARCHAR(20) NOT NULL,
    cardNumber VARCHAR(19) NOT NULL UNIQUE,
    FOREIGN KEY (customerID) REFERENCES customer(customerID)
);
""")

cur.execute("""
CREATE TABLE room (
    roomNumber SMALLINT(3) NOT NULL PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    type ENUM('single', 'double', 'triple', 'quadruple') NOT NULL,
    availability ENUM('available', 'unavailable') NOT NULL,
    floor TINYINT NOT NULL CHECK (floor = roomNumber DIV 100)
);
""")

cur.execute("""
CREATE TABLE package (
	packageID INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	description TEXT,
	price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    roomID SMALLINT(3),
    FOREIGN KEY (roomID) REFERENCES room(roomNumber)
);
""")

cur.execute("""
CREATE TABLE transport (
	transportID INT AUTO_INCREMENT PRIMARY KEY,
	type ENUM('shuttle', 'train', 'helicopter', 'snowmobile') NOT NULL,
	price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
	timetable TEXT
);
""")

# Junction table for the many to many relationship between package and transport
cur.execute("""
CREATE TABLE package_transportation (
    packageID INT,
    transportID INT,
    PRIMARY KEY (packageID, transportID),
    FOREIGN KEY (packageID) REFERENCES package(packageID) ON DELETE CASCADE,
    FOREIGN KEY (transportID) REFERENCES transport(transportID) ON DELETE CASCADE
);
""")

cur.execute("""
CREATE TABLE (

);
""")

# cur.execute("""
# CREATE TABLE (

# );
# """)

# TODO: totalCost should become a derived attribute later
cur.execute("""
CREATE TABLE reservation (
    reservationID INT PRIMARY KEY AUTO_INCREMENT,
    status ENUM('pending', 'confirmed', 'cancelled', 'completed', 'no_show', 'expired', 'failed') NOT NULL,
    paymentStatus ENUM('payed', 'unpayed', 'failed') NOT NULL,
    checkInDate DATE NOT NULL,
    checkOutDate DATE NOT NULL,
    totalCost DECIMAL(10, 2) NOT NULL CHECK (totalCost > 0),
    hotelID INT,
    customerID INT,
    roomID SMALLINT(3),
    FOREIGN KEY (hotelID) REFERENCES hotel(hotelID),
    FOREIGN KEY (customerID) REFERENCES customer(customerID),
    FOREIGN KEY (roomID) REFERENCES room(roomNumber)
);
""")

# cur.execute("""
# CREATE TABLE skiResort (
# 	resortID INT AUTO_INCREMENT PRIMARY KEY,
# 	name VARCHAR(100),
# 	size FLOAT(4, 2) CHECK (size > 0),
# 	location VARCHAR(255),
# 	difficultyLevel ENUM('Beginner', 'Intermediate', 'Advanced', 'Expert'),
# 	skiLiftsCount SMALLINT CHECK (skiLiftsCount > 0),
# 	slopesCount TINYINT CHECK (slopesCount > 0)
# );
# """)

# cur.execute("""
# CREATE TABLE skiPass (
# 	skiPassID INT AUTO_INCREMENT PRIMARY KEY,
# 	price DECIMAL(10, 2) CHECK (price > 0),
# 	startDate DATETIME,
# 	endDate DATETIME,
# 	validityPeriod INTEGER CHECK (validityPeriod > 0),
# 	CHECK (endDate >= startDate),
# 	CHECK (validityPeriod = DATEDIFF(DAY, endDate, startDate))
# );
# """)