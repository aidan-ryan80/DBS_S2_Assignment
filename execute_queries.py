# Module Imports
import mariadb
import sys
from tabulate import tabulate
#py -m pip install tabulate

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

    # Selecting all reservations that have been confirmed and payed:
    cursor.execute("""
    SELECT * FROM Reservations R 
    WHERE R.status = "confirmed" 
    AND R.paymentStatus = "payed";
    """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
else:
    print("\nDatabase SkiHotelDB does not exist\n")

cursor.close()
conn.close()