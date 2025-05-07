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

# Disable foreign key checks
cur.execute("SET FOREIGN_KEY_CHECKS = 0;")

tables = ["package_transport", "reservation", "package", "reservation", "paymentInfo", "transport", "room", "customer", "hotel"]

for table in tables:
    cur.execute(f"DROP TABLE IF EXISTS {table};")