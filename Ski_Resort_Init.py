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

# TODO: totalCost should become a derived attribute later
cur.execute("""
CREATE TABLE reservation (
    reservationID INT PRIMARY KEY AUTO_INCREMENT,
    status ENUM('pending', 'confirmed', 'cancelled', 'completed', 'no_show', 'expired', 'failed'),
    paymentStatus ENUM('payed', 'unpayed', 'failed'),
    checkInDate DATE NOT NULL,
    checkOutDate DATE NOT NULL,
    totalCost DECIMAL(10, 2),
    hotelID INT,
    customerID INT,
    FOREIGN KEY (hotelID) REFERENCES hotel(hotelID),
    FOREIGN KEY (customerID) REFERENCES customer(customerID),
);
""")

cur.execute("""
CREATE TABLE hotel (
    hotelID INT PRIMARY KEY AUTO_INCREMENT,
    address VARCHAR(100) NOT NULL, 
    name VARCHAR(100) NOT NULL,
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
    address VARCHAR(100) NOT NULL,
);
""")

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

# Apparently for payment only certified payment processors should store credit card numbers, CVV codes, Expiration dates, and cardholder names. 
# Instead token or ID's are stored and referenced. For now I will include payment information for the customer, and each reservation

# Could have a Table for Emails, so that a user can have multiple emails associated with them (work, personal), or we can implement only a single email.
# cur.execute("""
# CREATE TABLE Emails (id INT PRIMARY KEY AUTO_INCREMENT,
#     userID INT, 
#     email VARCHAR(100) UNIQUE NOT NULL, 
#     FOREIGN KEY (userID) REFERENCES Customer(customerID)
# );
# """)