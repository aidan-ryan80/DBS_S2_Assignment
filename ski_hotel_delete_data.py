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
cur = conn.cursor()

# Checking if the SkiHotelDB exists
cur.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'SkiHotelDB';")
if cur.fetchone():
    cur.execute("USE SkiHotelDB;")

    # Disabling foreign key checks for truncating all tables
    cur.execute("SET FOREIGN_KEY_CHECKS = 0;")

    tables = ["PackagesTransports", "Reservations", "Packages", "SkiPasses", "SkiResorts", "BusinessHours", "PaymentInfos", "Transports", "Rooms", "Customers", "Hotel"]

    for table in tables:
        cur.execute(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'SkiHotelDB' AND TABLE_NAME = '{table}';")
        if cur.fetchone():
            cur.execute(f"TRUNCATE TABLE `{table}`;")

else:
    print("\nDatabase SkiHotelDB does not exist\n")