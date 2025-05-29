import psycopg2
#sqlalchemy ? to avoid error from pandas when reading sql
import pandas as pd
import matplotlib.pyplot as plt

connection_uri = "postgres://postgres:superpass@localhost:5433/testDB"

try:
    with psycopg2.connect(connection_uri) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            result = cursor.fetchone()
            print("Connection successful, query result:", result)

            # For some reason queries show only 24 rows of scan data even when the loop for fake scanning has iterated 1000 times.

            # cursor.execute("SELECT s.skipassid, s.passtype, s.customerid, s.customer_name, s.reservationid, s.resort_name FROM scans_per_ten_seconds s")

            # Number of times each customers ski pass was scanned:
            # SELECT customerid, customer_name, COUNT(*) AS scans_for_customer
            # FROM scans_per_ten_seconds
            # GROUP BY customerid, customer_name
            # ORDER BY scans_for_customer DESC;

            # Number of times each ski pass was scanned:
            # SELECT skipassid, COUNT(*) AS scans_for_skipass
            # FROM scans_per_ten_seconds
            # GROUP BY skipassid
            # ORDER BY scans_for_skipass DESC;

            # Per reservation:
            # SELECT reservationid, COUNT(*) AS scans_for_reservation
            # FROM scans_per_ten_seconds
            # GROUP BY reservationid
            # ORDER BY scans_for_reservation DESC;

            #---Latest changes made---#
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
            
            # * Query with adding passtype and resort_name to the query:
            # ? How would we make this query work with the pandas visualization as well?
            # SELECT skipassid, passtype, resort_name, COUNT(*) AS scans_for_skipass
            # FROM scans_per_ten_seconds
            # GROUP BY skipassid, passtype, resort_name
            # ORDER BY scans_for_skipass DESC;

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

            # Query 5: Full scan data (your original request)
            #df_details = pd.read_sql("""
            #        SELECT bucket, passtype, skipassid, resort_name, customerid, customer_name, reservationid
            #        FROM scans_per_ten_seconds
            #        ORDER BY bucket;
            #    """, conn)
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

    # ---- Plotting Summary Visuals ----
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

    # ---- Plotting Time Series ----
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

    # ---- Print Full Scan Data ----
    print("\nFull Scan Detail Data ({} rows):".format(len(df_details)))
    print(df_details.to_string(index=False))

except psycopg2.Error as e:
    print("Connection failed:", e)

# * Commands for the project:
#  \q => exit DB
# psql "postgres://postgres:superpass@localhost:5433/testDB" 
# L==> For connecting to the containerized db running on port 5433 from local machine. 
# L==> Enters the database testDB right away as default user postgres with password superpass.
# \l => View all db
# \dt => View all tables in the db
# \c => Connect to database
# \d => View info about tables or relations

# * Hypertable chunks research:
# SELECT show_chunks('skipass_scans');
# SELECT show_chunks('scans_per_ten_seconds');

# It looks like the default chunk size in postgresql is 7 days, which is why our data will always fall into a single chunk. 
# We can either leave it, decrease the chunk size, or randomly select a date for the skipass scan instead of using current timestamps.

# "Explore and document the different chunks of your hypertable for different hypertable setups, using the following documentation:"
# "https://docs.timescale.com/api/latest/hypertable/show_chunks/"
# These instructions don't make much sense because different hypertable setups are not specified in the link given and the documentation
# just shows how to get different chunks associated with a table based off of conditions, but we only have a single chunk.

# * Continuous aggregate chunks:
# The continuous aggregate does not have chunks until a manual refresh is called because it is stored "on the fly in real time" according to George Paul.
# CALL refresh_continuous_aggregate() needs to be used to view the chunks for the continuous aggregate when data is very recent.