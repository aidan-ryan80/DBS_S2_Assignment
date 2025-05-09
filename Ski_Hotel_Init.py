# Module Imports
import mariadb
import sys
import time

time.sleep(5)

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
        age VARCHAR(50) DEFAULT NULL,
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
    CREATE TABLE IF NOT EXISTS skiResort (
        resortID INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        size FLOAT(4, 2) CHECK (size > 0),
        location VARCHAR(255),
        difficultyLevel ENUM('Beginner', 'Intermediate', 'Advanced', 'Expert'),
        skiLiftsCount SMALLINT CHECK (skiLiftsCount > 0),
        slopesCount SMALLINT CHECK (slopesCount > 0)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skiPass (
        skiPassID INT AUTO_INCREMENT PRIMARY KEY,
        price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
        startDate DATETIME NOT NULL,
        endDate DATETIME NOT NULL,
        validityPeriod INT AS (TIMESTAMPDIFF(DAY, startDate, endDate)) STORED,
        resortID INT,
        CHECK (validityPeriod > 0),
        FOREIGN KEY(resortID) REFERENCES skiResort(resortID)
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
    # We can decide to derive the totalCost for the reservation using a trigger, or we can remove the totalCost attribute and query the total cost from the DB using a view instead.
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

    payment_info_data = [
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
    cursor.executemany("INSERT INTO paymentInfo (customerID, billingAddress, cardHolderName, expirationDate, cardIssuer, cardNumber) VALUES (%s, %s, %s, %s, %s, %s)", payment_info_data)

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

    ski_pass_data = [
        (50.00, '2025-05-10 08:00:00', '2025-05-12 18:00:00', 1),  # 2 days
        (75.00, '2025-05-15 08:00:00', '2025-05-18 18:00:00', 2),  # 3 days
        (100.00, '2025-06-01 08:00:00', '2025-06-05 18:00:00', 2), # 4 days
        (120.00, '2025-06-10 08:00:00', '2025-06-15 18:00:00', 1), # 5 days
        (150.00, '2025-07-01 08:00:00', '2025-07-07 18:00:00', 3), # 6 days
        (200.00, '2025-07-15 08:00:00', '2025-07-22 18:00:00', 4), # 7 days
        (250.00, '2025-08-01 08:00:00', '2025-08-10 18:00:00', 5), # 9 days
        (300.00, '2025-08-15 08:00:00', '2025-08-25 18:00:00', 6), # 10 days
        (350.00, '2025-09-01 08:00:00', '2025-09-12 18:00:00', 7), # 11 days
        (400.00, '2025-09-15 08:00:00', '2025-09-30 18:00:00', 8)  # 15 days
    ]
    cursor.executemany("INSERT INTO skiPass (price, startDate, endDate, resortID) VALUES (%s, %s, %s, %s)", ski_pass_data)

    ski_resort_data = [
        ("Alpine Meadows", 45.50, "California, USA", "Intermediate", 13, 60),
        ("Snowbird", 50.75, "Utah, USA", "Advanced", 15, 85),
        ("Whistler Blackcomb", 82.30, "British Columbia, Canada", "Expert", 25, 200),
        ("Aspen Snowmass", 55.20, "Colorado, USA", "Intermediate", 21, 96),
        ("Zermatt", 70.00, "Valais, Switzerland", "Expert", 18, 150),
        ("Chamonix", 65.40, "Haute-Savoie, France", "Advanced", 20, 120),
        ("Cortina d'Ampezzo", 40.25, "Veneto, Italy", "Intermediate", 12, 50),
        ("Niseko", 38.10, "Hokkaido, Japan", "Beginner", 10, 40),
        ("Banff Sunshine", 48.60, "Alberta, Canada", "Advanced", 14, 75),
        ("St. Anton", 60.80, "Tyrol, Austria", "Expert", 22, 140)
    ]
    cursor.executemany("INSERT INTO skiResort (name, size, location, difficultyLevel, skiLiftsCount, slopesCount) VALUES (%s, %s, %s, %s, %s, %s)", ski_resort_data)

    package_data = [
        ('Package 1', 'Description of Package 1', 660.34, 5),
        ('Package 2', 'Description of Package 2', 1196.66, 7),
        ('Package 3', 'Description of Package 3', 287.4, 3),
        ('Package 4', 'Description of Package 4', 1247.75, 5),
        ('Package 5', 'Description of Package 5', 537.84, 2),
        ('Package 6', 'Description of Package 6', 1035.5, 5),
        ('Package 7', 'Description of Package 7', 553.64, 3),
        ('Package 8', 'Description of Package 8', 644.21, 3),
        ('Package 9', 'Description of Package 9', 593.46, 2),
        ('Package 10', 'Description of Package 10', 720.74, 3)
    ]
    cursor.executemany("INSERT INTO package (name, description, price, roomID, skiPassID) VALUES (%s, %s, %s, %s, %s)", package_data)

    transport_data = [
        ('shuttle', 15.00, "Mon-Fri: 08:00-18:00, Sat-Sun: 09:00-17:00"),
        ('train', 25.00, "Daily: 06:00-22:00"),
        ('helicopter', 150.00, "On-Demand: 08:00-20:00"),
        ('snowmobile', 50.00, "Mon-Fri: 07:00-19:00"),
        ('shuttle', 18.00, "Sat-Sun: 09:00-21:00"),
        ('train', 22.00, "Mon-Fri: 05:30-23:30"),
        ('helicopter', 175.00, "Daily: 08:00-18:00"),
        ('snowmobile', 55.00, "Weekends: 06:00-20:00"),
        ('shuttle', 20.00, "Daily: 07:00-22:00"),
        ('train', 30.00, "Daily: 04:30-00:00")
    ]
    cursor.executemany("INSERT INTO table (type, price, timetable) VALUES (%s, %s, %s)", transport_data)

    package_transport_data = [
        (5, 5),
        (8, 4),
        (4, 3),
        (9, 9),
        (7, 10),
        (8, 10),
        (5, 10),
        (4, 5),
        (1, 7),
        (8, 3)
    ]
    cursor.executemany("INSERT INTO table (attr1, attr2) VALUES (%s, %s)", package_transport_data)

    # (hotelID, roomID, customerID, packageID, startDate, endDate)
    reservation_data = [
        (1, 1, 1, 1, '2025-01-10', '2025-01-17'),
        (2, 2, 2, 2, '2025-02-05', '2025-02-12'),
        (3, 3, 3, 3, '2025-01-20', '2025-01-25'),
        (4, 4, 4, 4, '2025-01-15', '2025-01-22'),
        (5, 5, 5, 5, '2025-02-01', '2025-02-08'),
        (1, 6, 6, 6, '2025-03-10', '2025-03-17'),
        (2, 7, 7, 7, '2025-03-15', '2025-03-22'),
        (3, 8, 8, 8, '2025-01-05', '2025-01-12'),
        (4, 9, 9, 9, '2025-02-10', '2025-02-17'),
        (5, 10, 10, 10, '2025-03-01', '2025-03-08'),
    ]
    cursor.executemany("INSERT INTO reservation (hotelID, roomID, customerID, packageID, startDate, endDate) VALUES (%s, %s, %s, %s, %s, %s)", reservation_data)

# Checking if the SkiHotelDB exists and creating it if it does not.
cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'SkiHotelDB';")
if cursor.fetchone():
    cursor.execute("USE SkiHotelDB;")
    create_tables(cursor)
    # enter_data(cursor)
    conn.commit()

    print("\nSuccessfully created tables in SkiHotelDB Database if they did not exist\n")
else:
    cursor.execute("CREATE DATABASE SkiHotelDB;")
    cursor.execute("USE SkiHotelDB;")
    create_tables(cursor)
    # enter_data(cursor)
    conn.commit()

    print("\nSuccessfully created the SkiHotelDB Database and created required tables if they did not exist\n")