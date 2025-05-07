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

cur.execute("DROP TABLE paymentInfo;")
cur.execute("DROP TABLE reservation;")
cur.execute("DROP TABLE customer;")
cur.execute("DROP TABLE hotel;")
cur.execute("DROP TABLE room;")