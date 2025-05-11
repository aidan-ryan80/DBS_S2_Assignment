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

    # Disabling foreign key checks for deleting all of the tables
    cur.execute("SET FOREIGN_KEY_CHECKS = 0;")

    tables = ["PackagesTransports", "Reservations", "Packages", "SkiPasses", "SkiResorts", "BusinessHours", "PaymentInfos", "Transports", "Rooms", "Customers", "Hotel"]

    for table in tables:
        cur.execute(f"DROP TABLE IF EXISTS {table};")

    cur.execute("DROP DATABASE IF EXISTS SkiHotelDB;")
    print("\nDropped all of the tables in the SkiHotelDB if they existed\n")
else:
    print("\nDatabase SkiHotelDB does not exist\n")
