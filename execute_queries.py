# Module Imports
import mariadb
import sys
from tabulate import tabulate

# py -m pip install tabulate

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
    print()

    # List all customers who have booked a skipass as part of at least one of their future reservations (as of current date), sorted by the (combined) number of nights of their reservations (descending):
    cursor.execute("""
        SELECT c.customerID, c.name, SUM(DATEDIFF(r.checkOutDate, r.checkInDate)) AS total_nights, CURRENT_DATE AS as_of
        FROM Reservations r 
        JOIN Customers c ON r.customerID = c.customerID
        WHERE r.status = 'confirmed' AND r.checkInDate > CURRENT_DATE AND r.packageID IS NOT NULL
        GROUP BY c.customerID
        ORDER BY total_nights DESC;
        """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("List all customers who have booked a skipass as part of at least one of their future reservations, sorted by the (combined) number of nights of their reservations (descending):")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # Find the most often booked package:
    cursor.execute("""
        SELECT p.packageID, p.name, 
        COUNT(*) AS package_booking_count
        FROM Customers c
        JOIN Reservations r ON r.customerID = c.customerID
        JOIN Packages p ON r.packageID = p.packageID
        WHERE r.status != 'cancelled'
        GROUP BY p.packageID
        ORDER BY package_booking_count DESC
        LIMIT 1;
        """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("Find the most often booked package:")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()
 
    # Created just now:
    # SELECT R.reservationID, R.totalCost AS price_above_1000, R.status, R.paymentStatus, C.customerID, C.name FROM Reservations R JOIN Customers C ON R.customerID = C.customerID WHERE R.totalCost > 1000;
    # Retrieve all reservations with a total price above a certain threshold (in this case a total price more than 1000):
    threshold_price = 1000
    cursor.execute(f"""
        SELECT r.reservationID, r.totalCost AS price_above_1000, r.status, r.paymentStatus, c.customerID, c.name
        FROM Customers c
        JOIN Reservations r ON r.customerID = c.customerID
        WHERE r.totalCost > ?;
        """, (threshold_price,))
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(
        "Retrieve all reservations with a total price above a certain threshold (in this case a total price more than 1000):")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # ? How come this query give me 6426.00 as total reservation revenue between the defined dates?
    # SELECT SUM(R.totalCost) FROM Reservations R WHERE paymentStatus = "payed" AND checkOutDate BETWEEN "2025-05-01" AND "2026-01-01"; FOR reservation revenue
    # SELECT SUM(R.totalCost) FROM Reservations R WHERE paymentStatus = "payed" AND checkOutDate BETWEEN "2025-05-01" AND "2026-01-01" AND R.packageID IS NOT NULL; FOR package revenue

    # Find the total revenue from package sales within a predefined date range (in this case between 2025-05-01 and 2026-01-01):
    lower_date_range = '2025-05-01'
    upped_date_range = '2026-01-01'
    cursor.execute("""
        SELECT COALESCE(SUM(package_prices), 0) AS packages_total_revenue, COALESCE(SUM(reservations_total_costs), 0)  AS reservations_total_revenue
        FROM (SELECT p.price AS package_prices, r.totalCost AS reservations_total_costs
        FROM Customers c
        JOIN Reservations r ON r.customerID = c.customerID
        JOIN Packages p ON r.packageID = p.packageID
        WHERE r.status != 'cancelled' AND r.status != 'unpayed' AND r.checkInDate >= ? AND r.checkOutDate <= ?)
        AS packages;
        """, (lower_date_range, upped_date_range))
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(
        "Find the total revenue from package sales within a predefined date range (in this case between 2025-05-01 and 2026-01-01):")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # The most frequently used room vs the least frequently used room:
    cursor.execute("""
        SELECT * FROM (
        SELECT rm.roomNumber AS most_used_room, rm.price AS most_used_room_price,
        COUNT(*) AS room_usage
        FROM Customers c
        JOIN Reservations r ON r.customerID = c.customerID
        JOIN Rooms rm ON r.roomID = rm.roomNumber
        WHERE r.status = 'completed'
        GROUP BY rm.roomNumber
        ORDER BY room_usage DESC
        LIMIT 1) AS most_frequently_used
        JOIN 
        (SELECT rm.roomNumber AS least_used_room, rm.price AS least_used_room_price,
        COUNT(*) AS room_usage
        FROM Customers c
        JOIN Reservations r ON r.customerID = c.customerID
        JOIN Rooms rm ON r.roomID = rm.roomNumber
        WHERE r.status = 'completed'
        GROUP BY rm.roomNumber
        ORDER BY room_usage ASC
        LIMIT 1) AS least_frequently_used;
        """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("The most frequently used room vs the least frequently used room:")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # Selecting all reservations that have been confirmed and payed:
    cursor.execute("""
    SELECT R.reservationID, R.status, R.paymentStatus, R.checkInDate, R.checkOutDate, R.totalCost, R.packageID, R.roomID AS room
    FROM Reservations R 
    WHERE R.status = "confirmed" 
    AND R.paymentStatus = "payed";
    """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("All reservations that have been confirmed and payed:")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # Selecting all customers that have not payed for their reservations yet in order to send Debt collectors after them:
    cursor.execute("""
    SELECT DISTINCT C.customerID, C.email, C.phoneNumber, C.name, C.age, C.address
    FROM Customers C 
    JOIN Reservations R ON R.customerID = C.CustomerID 
    WHERE R.paymentStatus = "unpayed"
    ORDER BY C.customerID;
    """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("All customers that have not payed for their reservations yet in order to send Debt collectors after them:")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # Querying for the total income our evil Ski Hotel Monopoly has made in the first quarter:
    cursor.execute("""
    SELECT COALESCE(SUM(R.totalCost), 0) AS first_quarter_income
    FROM Reservations R 
    WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-01-01' AND '2025-03-31';
    """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("Querying for the total income our evil Ski Hotel Monopoly has made in the first quarter:")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # Second Quarter Income:
    cursor.execute("""
    SELECT COALESCE(SUM(R.totalCost), 0) AS second_quarter_income
    FROM Reservations R 
    WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-04-01' AND '2025-06-30';
    """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("Second Quarter Income:")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # Third Quarter Income:
    cursor.execute("""
    SELECT COALESCE(SUM(R.totalCost), 0) AS third_quarter_income
    FROM Reservations R 
    WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-07-01' AND '2025-09-30';
    """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("Third Quarter Income:")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # Fourth Quarter Income:
    cursor.execute("""
    SELECT COALESCE(SUM(R.totalCost), 0) AS fourth_quarter_income
    FROM Reservations R 
    WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-10-01' AND '2025-12-31';
    """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("Fourth Quarter Income:")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # Financial Year 2025 Income:
    cursor.execute("""
    SELECT COALESCE(SUM(R.totalCost), 0) AS Financial_year_2025_income
    FROM Reservations R 
    WHERE R.paymentStatus = "payed" AND  checkInDate BETWEEN '2025-01-01' AND '2025-12-31';
    """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("Financial Year 2025 Income:")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()

    # Total amount not payed yet for Reservations
    cursor.execute("""
    SELECT COALESCE(SUM(R.totalCost), 0) AS reservations_unpaid_total_amount
    FROM Reservations R 
    WHERE R.paymentStatus = "unpayed" OR R.paymentStatus = "failed";
    """)
    all_rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print("Total amount not payed yet for Reservations")
    print(tabulate(all_rows, headers=headers, tablefmt='psql'))
    print()
else:
    print("\nDatabase SkiHotelDB does not exist\n")

cursor.close()
conn.close()

# TODO: Change confirmed reservations to payed