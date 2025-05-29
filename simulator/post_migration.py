import psycopg2

conn_info = {
    "dbname": "SkiHotelDB",
    "user": "postgres",
    "password": "superpass",
    "host": "timescaledb",
    "port": 5432
}

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
            
            cursor.execute("SELECT create_hypertable('skipass_scans', 'scan_time', chunk_time_interval => interval '10 seconds');")

            cursor.execute("""
                CREATE MATERIALIZED VIEW scans_per_ten_seconds
                WITH (timescaledb.continuous) AS 
                SELECT 
                    time_bucket('10 seconds', scan_time) AS bucket,
                    rsp.passtype,
                    rsp.skipassid,
                    sr.name AS resort_name,
                    sc.customerid,
                    c.name AS customer_name,
                    sc.reservationid,
                    r.checkindate,
                    r.checkoutdate
                FROM 
                    skipass_scans sc
                JOIN res_ski_passes rsp ON sc.res_skipass_id = rsp.id
                JOIN skiresorts sr ON sc.resortid = sr.resortid
                JOIN customers c ON sc.customerid = c.customerid
                JOIN reservations r ON sc.reservationid = r.reservationid
                GROUP BY bucket, rsp.passtype, rsp.skipassid, sr.name, sc.customerid, c.name, sc.reservationid, r.checkindate, r.checkoutdate
                WITH NO DATA;
            """)

            # Enabling real time aggregation
            cursor.execute("ALTER MATERIALIZED VIEW scans_per_ten_seconds set (timescaledb.materialized_only = false);")
            print("Created continuous aggregate")

            conn.commit()
except psycopg2.Error as e:
    print("Connection failed:", e)