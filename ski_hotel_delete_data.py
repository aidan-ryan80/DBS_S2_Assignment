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

# Checking if the SkiHotelDB exists
cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'SkiHotelDB';")
if cursor.fetchone():
    cursor.execute("USE SkiHotelDB;")

    # Disabling foreign key checks for truncating all tables
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

    tables = ["PackagesTransports", "Reservations", "Packages", "SkiPasses", "SkiResorts", "BusinessHours", "PaymentInfos", "Transports", "Rooms", "Customers", "Hotel"]

    for table in tables:
        cursor.execute(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'SkiHotelDB' AND TABLE_NAME = '{table}';")
        if cursor.fetchone():
            cursor.execute(f"TRUNCATE TABLE `{table}`;")

else:
    print("\nDatabase SkiHotelDB does not exist\n")

cursor.close()
conn.close()