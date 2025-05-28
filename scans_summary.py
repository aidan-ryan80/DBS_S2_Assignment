import psycopg2

connection_uri = "postgres://postgres:superpass@localhost:5433/testDB"

try:
    with psycopg2.connect(connection_uri) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            result = cursor.fetchone()
            print("Connection successful, query result:", result)
            
            # cursor.execute("SELECT s.skipassid, s.passtype, s.customerid, s.customer_name, s.reservationid, s.resort_name FROM skipasses_by_minute sbm")

            # Number of times each customers ski pass was scanned:
            # SELECT customerid, customer_name, COUNT(*) AS scans_for_customer
            # FROM skipasses_by_minute
            # GROUP BY customerid, customer_name
            # ORDER BY scans_for_customer DESC;

            # Number of times each ski pass was scanned:
            # SELECT skipassid, COUNT(*) AS scans_for_skipass
            # FROM skipasses_by_minute
            # GROUP BY skipassid
            # ORDER BY scans_for_skipass DESC;

            # Per reservation:
            # SELECT reservationid, COUNT(*) AS scans_for_reservation
            # FROM skipasses_by_minute
            # GROUP BY reservationid
            # ORDER BY scans_for_reservation DESC;

except psycopg2.Error as e:
    print("Connection failed:", e)

# * Commands for the project:
#  \q => exit DB
# psql "postgres://postgres:superpass@localhost:5433/testDB" => For connecting to the db from local machine to docker container
# \l => View all db
# \dt => View all tables in the db
# \c => Connect to database
# \d => View info about tables or relations