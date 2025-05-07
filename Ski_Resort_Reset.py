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

tables = ["paymentInfo", "reservation", "customer", "hotel", "package", "room", "skiResort", "skiPass", "transport"]

for table in tables:
    cur.execute(f"DROP TABLE IF EXISTS {table};")