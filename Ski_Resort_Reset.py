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

# Checking if the SkiResortDB exists
cur.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'SkiResortDB';")
if cur.fetchone():
    cur.execute("USE SkiResortDB;")

    # Disabling foreign key checks for deleting all of the tables
    cur.execute("SET FOREIGN_KEY_CHECKS = 0;")

    tables = ["packageTransport", "reservation", "package", "skiPass", "skiResort", "reservation", "paymentInfo", "transport", "room", "customer", "hotel"]

    for table in tables:
        cur.execute(f"DROP TABLE IF EXISTS {table};")

    cur.execute("DROP DATABASE IF EXISTS SkiResortDB;")
else:
    print("Database SkiResortDB does not exist.")
