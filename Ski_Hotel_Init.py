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
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Getting a Cursor
cursor = conn.cursor()

def create_tables(cursor) -> None:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hotel (
        hotelID INT PRIMARY KEY AUTO_INCREMENT,
        address VARCHAR(100) NOT NULL, 
        name VARCHAR(100) NOT NULL
    );
    """)

    # ? From email, name, age, address, and phoneNumber what should be NOT NULL?
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer (
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
    cursor.execute("""
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
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS room (
        roomNumber SMALLINT(3) NOT NULL PRIMARY KEY,
        price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
        type ENUM('single', 'double', 'triple', 'quadruple') NOT NULL,
        availability ENUM('available', 'unavailable') NOT NULL,
        floor TINYINT NOT NULL CHECK (floor = roomNumber DIV 100)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skiPass (
        skiPassID INT AUTO_INCREMENT PRIMARY KEY,
        price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
        startDate DATETIME NOT NULL,
        endDate DATETIME NOT NULL,
        validityPeriod INT AS (TIMESTAMPDIFF(DAY, startDate, endDate)) STORED,
        CHECK (validityPeriod > 0)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skiResort (
        resortID INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        size FLOAT(4, 2) CHECK (size > 0),
        location VARCHAR(255),
        difficultyLevel ENUM('Beginner', 'Intermediate', 'Advanced', 'Expert'),
        skiLiftsCount SMALLINT CHECK (skiLiftsCount > 0),
        slopesCount TINYINT CHECK (slopesCount > 0),
        skiPassID INT,
        FOREIGN KEY(skiPassID) REFERENCES skiPass(skiPassID)
    );
    """)

    cursor.execute("""
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
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transport (
        transportID INT AUTO_INCREMENT PRIMARY KEY,
        type ENUM('shuttle', 'train', 'helicopter', 'snowmobile') NOT NULL,
        price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
        timetable TEXT
    );
    """)

    # Junction table for the many to many relationship between package and transport
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS packageTransport (
        packageID INT,
        transportID INT,
        PRIMARY KEY (packageID, transportID),
        FOREIGN KEY (packageID) REFERENCES package(packageID) ON DELETE CASCADE,
        FOREIGN KEY (transportID) REFERENCES transport(transportID) ON DELETE CASCADE
    );
    """)

    # TODO: totalCost should become a derived attribute later
    cursor.execute("""
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
    """)

    # cur.execute("""
    # CREATE TABLE (

    # );
    # """)

def enter_data(cursor) -> None:
    # Inserting a single entry the hotel table.
    cursor.execute("INSERT INTO hotel (address, name) VALUES ('myaddress123, 2001, Vienna', 'Awesome Resort');")

    # Inserting 10 rows of data into the rest of the tables:
    customer_data = [
        ('john.doe@example.com', '1234567890', 'John Doe', '30', '123 Main St'),
        ('jane.smith@example.com', '0987654321', 'Jane Smith', '25', '456 Elm St'),
        ('alice.brown@example.com', '1122334455', 'Alice Brown', '28', '789 Oak St'),
        ('michael.johnson@example.com', '2233445566', 'Michael Johnson', '35', '321 Pine St'),
        ('emily.davis@example.com', '3344556677', 'Emily Davis', '27', '654 Maple St'),
        ('david.wilson@example.com', '4455667788', 'David Wilson', '40', '987 Birch St'),
        ('sarah.miller@example.com', '5566778899', 'Sarah Miller', '22', '159 Cedar St'),
        ('chris.moore@example.com', '6677889900', 'Chris Moore', '33', '753 Walnut St'),
        ('laura.taylor@example.com', '7788990011', 'Laura Taylor', '29', '852 Chestnut St'),
        ('daniel.anderson@example.com', '8899001122', 'Daniel Anderson', '31', '951 Spruce St')
    ]
    
    cursor.executemany("INSERT INTO customer (email, phoneNumber, name, age, address) VALUES (%s, %s, %s, %s, %s)", customer_data)

    paymentInfo_data = [
        (1, '123 Main St', 'John Doe', '2025-12-31', 'Visa', '4111111111111111'),
        (2, '456 Elm St', 'Jane Smith', '2026-06-30', 'MasterCard', '5500000000000004'),
        (3, '789 Oak St', 'Alice Brown', '2024-09-15', 'American Express', '340000000000009'),
        (4, '321 Pine St', 'Michael Johnson', '2027-03-20', 'Discover', '6011000000000004'),
        (5, '654 Maple St', 'Emily Davis', '2025-11-10', 'Visa', '4111111111111234'),
        (6, '987 Birch St', 'David Wilson', '2026-01-25', 'MasterCard', '5500000000005678'),
        (7, '159 Cedar St', 'Sarah Miller', '2024-07-05', 'American Express', '340000000000567'),
        (8, '753 Walnut St', 'Chris Moore', '2027-02-14', 'Discover', '6011000000007890'),
        (9, '852 Chestnut St', 'Laura Taylor', '2025-08-19', 'Visa', '4111111111113456'),
        (10, '951 Spruce St', 'Daniel Anderson', '2026-04-30', 'MasterCard', '5500000000007890')
    ]

    cursor.executemany("INSERT INTO paymentInfo (customerID, billingAddress, cardHolderName, expirationDate, cardIssuer, cardNumber) VALUES (%s, %s, %s, %s, %s, %s)", paymentInfo_data)

    room_data = [
        (100, 100.00, 'single', 'available', 1),
        (101, 120.00, 'double', 'available', 1),
        (199, 150.00, 'triple', 'unavailable', 1),
        (200, 180.00, 'quadruple', 'available', 2),
        (201, 90.00, 'single', 'available', 2),
        (299, 110.00, 'double', 'unavailable', 2),
        (300, 200.00, 'quadruple', 'available', 3),
        (301, 170.00, 'triple', 'unavailable', 3),
        (399, 95.00, 'single', 'available', 3),
        (400, 125.00, 'double', 'available', 4)
    ]
    cursor.executemany("INSERT INTO room (roomNumber, price, type, availability, floor) VALUES (%s, %s, %s, %s, %s)", room_data)

    skiPass_data = [
        (50.00, '2025-05-10 08:00:00', '2025-05-12 18:00:00'),  # 2 days
        (75.00, '2025-05-15 08:00:00', '2025-05-18 18:00:00'),  # 3 days
        (100.00, '2025-06-01 08:00:00', '2025-06-05 18:00:00'), # 4 days
        (120.00, '2025-06-10 08:00:00', '2025-06-15 18:00:00'), # 5 days
        (150.00, '2025-07-01 08:00:00', '2025-07-07 18:00:00'), # 6 days
        (200.00, '2025-07-15 08:00:00', '2025-07-22 18:00:00'), # 7 days
        (250.00, '2025-08-01 08:00:00', '2025-08-10 18:00:00'), # 9 days
        (300.00, '2025-08-15 08:00:00', '2025-08-25 18:00:00'), # 10 days
        (350.00, '2025-09-01 08:00:00', '2025-09-12 18:00:00'), # 11 days
        (400.00, '2025-09-15 08:00:00', '2025-09-30 18:00:00')  # 15 days
    ]
    
    cursor.executemany("INSERT INTO skiPass (price, startDate, endDate) VALUES (%s, %s, %s)", skiPass_data)

    # data = []
    # cursor.executemany("INSERT INTO table (attr1, attr2) VALUES (%s, %s)", data)

# Checking if the SkiHotelDB exists and creating it if it does not.
cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'SkiHotelDB';")
if cursor.fetchone():
    cursor.execute("USE SkiHotelDB;")
    create_tables(cursor)
    enter_data(cursor)
    conn.commit()

    print("\nSuccessfully created tables in SkiHotelDB Database if they did not exist\n")
else:
    cursor.execute("CREATE DATABASE SkiHotelDB;")
    cursor.execute("USE SkiHotelDB;")
    create_tables(cursor)
    enter_data(cursor)
    conn.commit()

    print("\nSuccessfully created the SkiHotelDB Database and created required tables if they did not exist\n")
