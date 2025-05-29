import psycopg2
import random
import time
import json
from datetime import datetime, timedelta

conn_info = {
    "dbname": "testDB",
    "user": "postgres",
    "password": "superpass",
    "host": "timescaledb",
    "port": 5432
}

connection_uri = "postgres://postgres:superpass@localhost:5433/testDB"

try:
    with psycopg2.connect(**conn_info) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            result = cursor.fetchone()
            print("Connection successful, query result:", result)

            cursor.execute("""
                SELECT rsp.id, r.customerid, r.reservationid, rsp.resortid, sr.name, rsp.skipassid FROM res_ski_passes rsp 
                JOIN reservations r ON rsp.reservationid = r.reservationid 
                JOIN skiresorts sr ON rsp.resortid = sr.resortid;
            """)
            ski_pass_data = cursor.fetchall()

            if not ski_pass_data:
                raise ValueError("No ski pass data found to simulate scans.")
            
            batch_size: int = 10
            for i in range(1000):
                rand_scan = random.choice(ski_pass_data)
                scan_data = {
                    "res_skipass_id": rand_scan[0], 
                    "customer_id": rand_scan[1],
                    "reservation_id": rand_scan[2], 
                    "resort_id": rand_scan[3], 
                    "resort_name": rand_scan[4],
                    "skipass_id": rand_scan[5],
                    "timestamp": (datetime.now() + timedelta(hours=2)).isoformat()
                    }
                print(f"Scan: {json.dumps(scan_data)}")
                
                cursor.execute(
                    "INSERT INTO skipass_scans (scan_time, res_skipass_id, resortid, customerid, reservationid) VALUES (%s, %s, %s, %s, %s)",
                    (scan_data["timestamp"], scan_data["res_skipass_id"], scan_data["resort_id"], scan_data["customer_id"], scan_data["reservation_id"]))
                
                if i % batch_size == 0:
                    conn.commit()
                    # * Commented the manual refresh out because I enabled real-time aggregation by running the SQL code on line 87 in post_migration.py
                    # # Manually refresh aggregate outside of transaction block
                    # refresh_conn = psycopg2.connect(**conn_info)
                    # refresh_conn.autocommit = True
                    # refresh_cursor = refresh_conn.cursor()
                    # try:
                    #     refresh_cursor.execute(
                    #         "CALL refresh_continuous_aggregate('scans_per_ten_seconds', NULL, NULL);")
                    #     print("Manually refreshed aggregate")
                    # finally:
                    #     refresh_cursor.close()
                    #     refresh_conn.close()

                time.sleep(random.uniform(0.01, 0.50)) #Simulate different scan rate
                #time.sleep(0.01)
                # Sleep time extinguished for testing purposes (will be turned on again later)

except psycopg2.Error as e:
    print("Connection failed:", e)