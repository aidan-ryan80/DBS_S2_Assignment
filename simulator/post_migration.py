import psycopg2

conn_info = {
    "dbname": "testDB",
    "user": "postgres",
    "password": "superpass",
    "host": "timescaledb",
    "port": 5432
}

# connection_uri = "postgres://postgres:superpass@localhost:5433/testDB"

try:
    with psycopg2.connect(**conn_info) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            result = cursor.fetchone()
            print("Connection successful, query result:", result)

            cursor.execute("""
                           CREATE TABLE skipass_scans (
                           scan_time TIMESTAMPTZ NOT NULL, 
                           skipassid INT NOT NULL, 
                           resortid INT NOT NULL, 
                           customerid INT NOT NULL, 
                           reservationid INT NOT NULL, 
                           PRIMARY KEY (scan_time, skipassid, customerid), 
                           CONSTRAINT fk_skipass FOREIGN KEY (skipassid) REFERENCES skipasses(skipassid), 
                           CONSTRAINT fk_resort FOREIGN KEY (resortid) REFERENCES skiresorts(resortid), 
                           CONSTRAINT fk_customer FOREIGN KEY (customerid) REFERENCES customers(customerid), 
                           CONSTRAINT fk_reservation FOREIGN KEY (reservationid) REFERENCES reservations(reservationid));
                           """)
            
            cursor.execute("SELECT create_hypertable('skipass_scans', 'scan_time');")
            conn.commit()
except psycopg2.Error as e:
    print("Connection failed:", e)