import psycopg2

conn_info = {
    "dbname": "testDB",
    "user": "postgres",
    "password": "superpass",
    "host": "timescaledb",
    "port": 5432
}

# For running the python script manually on the postgreSQL DB:
# conn_info = {
#     "dbname": "testDB",
#     "user": "postgres",
#     "password": "superpass",
#     "host": "localhost",
#     "port": 5433
# }

# connection_uri = "postgres://postgres:superpass@localhost:5433/testDB"

# TODO: Add changing the skipass table to this script
# * Ended up doing:
# Created a res_ski_passes table that has a unique ski pass for each reservation. The data from the database is queried and a copy of the ski pass associated with the reservation is made 
# with the unique reservation id added onto it to be able to distinguish between different reservations having the same package and thus the same original ski pass.
# The option recommended by Daniel would not have worked because adding a reservationid to each skipass would require a new ski pass to be added each time a reservation is made, 
# which would have been redundant and required a trigger.

# TODO: Continuous Aggregates Python Script
# TODO: Explore and document the different chunks of your hypertable for different hypertable setups, using the following documentation

try:
    with psycopg2.connect(**conn_info) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            result = cursor.fetchone()
            print("Connection successful, query result:", result)

            cursor.execute("""
                CREATE TABLE res_ski_passes (
                id SERIAL PRIMARY KEY, 
                reservationid INT NOT NULL, 
                skipassid INT NOT NULL,
                resortid INT, 
                passType VARCHAR(20) CHECK (passType IN ('Day Pass', '2 Day Pass', '3 Day Pass', '4 Day Pass', '5 Day Pass', '6 Day Pass', '7 Day Pass')), 
                price NUMERIC(10, 2) NOT NULL CHECK (price > 0), 
                FOREIGN KEY (resortid) REFERENCES skiresorts(resortid), 
                FOREIGN KEY (reservationid) REFERENCES reservations(reservationid));
            """)

            cursor.execute("SELECT r.reservationid, s.skipassid, s.resortid, s.passtype, s.price FROM reservations r JOIN packages p ON r.packageid = p.packageid JOIN skipasses s ON p.skipassid = s.skipassid;")
            res_data = cursor.fetchall()
            
            cursor.executemany("INSERT INTO res_ski_passes (reservationid, skipassid, resortid, passType, price) VALUES (%s, %s, %s, %s, %s)", res_data)

            cursor.execute("""
                CREATE TABLE skipass_scans (
                scan_time TIMESTAMPTZ NOT NULL, 
                res_skipass_id INT NOT NULL, 
                resortid INT NOT NULL, 
                customerid INT NOT NULL, 
                reservationid INT NOT NULL, 
                PRIMARY KEY (scan_time, res_skipass_id, customerid), 
                CONSTRAINT fk_skipass FOREIGN KEY (res_skipass_id) REFERENCES res_ski_passes(id), 
                CONSTRAINT fk_resort FOREIGN KEY (resortid) REFERENCES skiresorts(resortid), 
                CONSTRAINT fk_customer FOREIGN KEY (customerid) REFERENCES customers(customerid), 
                CONSTRAINT fk_reservation FOREIGN KEY (reservationid) REFERENCES reservations(reservationid));
            """)
            
            cursor.execute("SELECT create_hypertable('skipass_scans', 'scan_time');")

            # Create continuous aggregate
            cursor.execute("""
                CREATE MATERIALIZED VIEW IF NOT EXISTS scans_per_user_reservation
                WITH (timescaledb.continuous) AS
                SELECT
                    time_bucket('10 seconds', scan_time) AS bucket,
                    customerid,
                    reservationid,
                    COUNT(*) AS scan_count
                FROM
                    skipass_scans
                GROUP BY bucket, customerid, reservationid
                WITH NO DATA;
            """)
            print("Created continuous aggregate")

            conn.commit()
except psycopg2.Error as e:
    print("Connection failed:", e)