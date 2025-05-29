import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

connection_uri = "postgres://postgres:superpass@localhost:5433/testDB"

try:
    with psycopg2.connect(connection_uri) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            result = cursor.fetchone()
            print("Connection successful, query result:", result)

            # Query 1: Scans per customer
            df_customer = pd.read_sql("""
                    SELECT customerid, customer_name, COUNT(*) AS scans_for_customer
                    FROM scans_per_ten_seconds
                    GROUP BY customerid, customer_name
                    ORDER BY scans_for_customer DESC;
                """, conn)

            # Query 2: Scans per skipass
            df_skipass = pd.read_sql("""
                    SELECT skipassid, passtype, resort_name, COUNT(*) AS scans_for_skipass
                    FROM scans_per_ten_seconds
                    GROUP BY skipassid, passtype, resort_name
                    ORDER BY scans_for_skipass DESC;
                """, conn)

            # Query 3: Scans per reservation
            df_reservation = pd.read_sql("""
                    SELECT reservationid, COUNT(*) AS scans_for_reservation
                    FROM scans_per_ten_seconds
                    GROUP BY reservationid
                    ORDER BY scans_for_reservation DESC;
                """, conn)

            # Query 4: Time series - count of scans per time bucket
            df_timeseries = pd.read_sql("""
                    SELECT bucket, COUNT(*) AS scan_count
                    FROM scans_per_ten_seconds
                    GROUP BY bucket
                    ORDER BY bucket;
                """, conn)

            # Query 5: Full scan data grouped by a 10-second time interval
            df_details = pd.read_sql("""
                    SELECT 
                    TO_CHAR(bucket, 'HH24:MI:SS') || ' - ' || TO_CHAR(bucket + INTERVAL '10 seconds', 'HH24:MI:SS') AS interval_range,
                    COUNT(*) AS scan_count
                    FROM scans_per_ten_seconds
                    GROUP BY bucket
                    ORDER BY bucket;
                """, conn)

            # 6. Show hypertable chunks
            cursor.execute("SELECT show_chunks('skipass_scans');")
            chunk_names = cursor.fetchall()
            print("\n Hypertable Chunks:")
            for chunk in chunk_names:
                print(" -", chunk[0])

    # ---- Plotting Summary Visuals ---- #
    plt.figure(figsize=(18, 6))

    # 1. Customers
    plt.subplot(1, 3, 1)
    plt.barh(df_customer["customer_name"], df_customer["scans_for_customer"], color="skyblue")
    plt.xlabel("Scan Count")
    plt.title("Scans per Customer")

    # 2. Skipasses
    plt.subplot(1, 3, 2)
    plt.barh(df_skipass["skipassid"].astype(str), df_skipass["scans_for_skipass"], color="orange")
    plt.xlabel("Scan Count")
    plt.title("Scans per Skipass")

    # 3. Reservations
    plt.subplot(1, 3, 3)
    plt.barh(df_reservation["reservationid"].astype(str), df_reservation["scans_for_reservation"], color="green")
    plt.xlabel("Scan Count")
    plt.title("Scans per Reservation")

    plt.tight_layout()
    plt.show()

    # ---- Plotting Time Series ---- #
    plt.figure(figsize=(10, 5))
    df_timeseries["bucket"] = pd.to_datetime(df_timeseries["bucket"])
    plt.plot(df_timeseries["bucket"], df_timeseries["scan_count"], marker="o", linestyle="-", color="purple")
    plt.xlabel("Time Bucket")
    plt.ylabel("Scans")
    plt.title("Ski Pass Scans Over Time (10s intervals)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # ---- Print Full Scan Data ---- #
    print("\nFull Scan Detail Data ({} rows):".format(len(df_details)))
    print(df_details.to_string(index=False))

except psycopg2.Error as e:
    print("Connection failed:", e)