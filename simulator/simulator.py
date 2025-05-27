import psycopg2
import random
import time
import json
from datetime import datetime

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
                           SELECT r.customerid, r.reservationid, p.skipassid, s.resortid, sr.name FROM reservations r 
                           JOIN packages p ON r.packageid = p.packageid 
                           JOIN skipasses s ON p.skipassid = s.skipassid 
                           JOIN skiresorts sr ON s.resortid = sr.resortid;
                           """)
            ski_pass_data = cursor.fetchall()

            if not ski_pass_data:
                raise ValueError("No ski pass data found to simulate scans.")
            
            batch_size: int = 10
            
            for i in range(10000):
                rand_scan = random.choice(ski_pass_data)
                scan_data = {
                    "customer_id": rand_scan[0],
                    "reservation_id": rand_scan[1], 
                    "skipass_id": rand_scan[2], 
                    "resort_id": rand_scan[3], 
                    "resort_name": rand_scan[4],
                    "timestamp": datetime.now().isoformat()
                    }
                print(json.dumps(scan_data))
                
                cursor.execute(
                    "INSERT INTO skipass_scans (scan_time, skipassid, resortid, customerid, reservationid) VALUES (%s, %s, %s, %s, %s)",
                    (scan_data["timestamp"], scan_data["skipass_id"], scan_data["resort_id"], scan_data["customer_id"], scan_data["reservation_id"]))
                
                if i % batch_size == 0:
                    conn.commit()
                
                time.sleep(1)

except psycopg2.Error as e:
    print("Connection failed:", e)