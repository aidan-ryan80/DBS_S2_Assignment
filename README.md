# DBS_S2_Assignment
##### Database Systems Assignment for Semester 2 of the IMC Bachelor’s Program in Computer Science

## 📌 Introduction
This assignment involves developing a **MariaDB database** for a hotel that specializes in customers on skiing trips. An **Entity Relationship Diagram (ERD)** was designed beforehand and is included in this repository. Note: the ERD does not include three entities that were later added during implementation.

---

## 📦 Python Dependencies

Before running any Python scripts, install the required packages using the following command:

```bash
pip install -r assignment_requirements.txt
```

If you prefer to not install them globally you can fist also create a python virtual environment.

These packages are needed for:
- Connecting to the MariaDB database (`mariadb`)
- Displaying query results in table format (`tabulate`)
- Connecting to the postgreSQL database (`psycopg2`)

## **Assignment 02**

## 🛠️ How to run the Assignment

### Method 1: Using `docker-compose`
1. Navigate to the project root directory:  
   ```bash
   cd DBS_S2_Assignment
   ```
2. Run the containers:  
   ```bash
   docker-compose -f docker-compose-02.yml up
   ```
   - This uses the MariaDB 10.3 image and initializes the database using the `.sql` files in the `init/` directory (executed in alphabetical order).
3. To enter the MariaDB shell:  
   ```bash
   docker exec -it SkiHotelDB_01 mysql -u root -p
   ```
   - Password: `rootpass` (defined in `docker-compose.yml`)
   - The `SkiHotelDB` database will already exist and be accessible.
4. Python scripts included in the repo:
   - `ski_hotel_init.py`: creates all tables and inserts initial data.
   - `execute_queries.py`: sample queries for testing the database.
   - `ski_hotel_delete_data.py`: truncates all tables.
   - `ski_hotel_reset.py`: drops all tables.
5. To stop and clean up:
   ```bash
   docker-compose -f docker-compose-02.yml down -v
   ```
   - Stops and removes containers, images, and **volumes**.

---

### Method 2: Using Dockerfile
1. Navigate to the project root:
   ```bash
   cd DBS_S2_Assignment
   ```
2. Build the image:
   ```bash
   docker build -t <image-name> .
   ```
3. Run a container:
   ```bash
   docker run -d --name <container-name> -p 3306:3306 <image-name>
   ```
4. Check if it’s running:
   ```bash
   docker ps
   ```
5. Enter the MariaDB shell:
   ```bash
   docker exec -it <container-name> mysql -u root -p
   ```
   - Password: `rootpass` (defined in the Dockerfile)

6. Use the same Python scripts listed in step 4 of the docker-compose method for testing, resetting, and developing.

7. To stop and clean up manually:
   ```bash
   docker stop <container-name>
   docker rm <container-name>
   docker image rm <image-name>
   docker volume prune
   ```

---

---

## ▶️ Running Python Scripts

To execute any of the included Python files, use the following command format:

```bash
python filename.py
```

Python files used in Assignment 02:

1. execute_queries.py
- This python file can be used to execute default queries on the database.

2. ski_hotel_delete_data.py (Optional)
- This file can be used to delete all data in all of the tables

3. ski_hotel_reset.py (Optional)
- This file resets the database to its initial state

4. ski_hotel_init.py
- This is the python file used by the dockerfile to initialize the database when using the dockerfile method.

Ensure the MariaDB container is running before executing these scripts.

---

## 🧠 About the Database Design

### Trigger Logic

- **Reservation Trigger (`set_reservation_price`)**  
  - Automatically calculates the total price before inserting a reservation.
  - Based on: room price (per night) + package price (if applicable).

- **Package Trigger (`set_package_price`)**  
  - Sets package price based on the ski pass associated with it before insertion.

- **PackagesTransports Trigger (`add_transport_price`)**  
  - Updates the package’s price **after** inserting into the `PackagesTransports` junction table.
  - Reflects the added transport cost in the many-to-many relationship.

- **PackagesTransports Trigger (`subtract_transport_price`)**  
  - Reverses the above logic **after** a deletion from the junction table.

> 🔎 Additional constraints like preventing room booking overlaps via triggers were considered, but not implemented due to time constraints.

## **Assignment 03**

## 🛠️ How to run the Assignment

### Using `docker-compose`
1. Navigate to the project root directory:  
   ```bash
   cd DBS_S2_Assignment
   ```
2. Run the containers:  
   ```bash
   docker-compose -f docker-compose-03.yml up
   ```
   - This runs 4 services the **MariaDB**, **postgresql**, **pgloader**, and **python** service.
   - The **pgloader** service migrates the database schema in the **MariaDB** service from the second assignment to the database in the **postgresql** service.
   - The **python** service runs the **simulator.py** and **post_migration.py** scripts. The **simulator.py** script is run to simulate ski passes being scanned, which are automatically inserted into the database in the **postgresql** service, while the **post_migration.py** script is run before the **simulator.py** script in order to update the database schema for using a hypertable and a continuous aggregate.
3. To view a summary of the data in the **postgresql** database run:
	```bash
	python scans_summary.py
	```
- This will show summary graphs of the data from the continuous aggregate.
- Also, it will print the chunks used by the hypertable and the rate at which ski pass scans occurred.
4. In order to look at our database schema you can use the psql shell either from you local machine if you have psql installed or inside of the **postgresql** service. 
	- Accessing the psql shell if you have it on your machine:
	```bash
    psql "postgres://postgres:superpass@localhost:5433/testDB"
	```
	- Accessing the psql shell inside of the docker container:
	```bash
	docker exec -it SkiHotelPSQLDB psql -U postgres
	```
5. To stop and clean up:
   ```bash
   docker-compose -f docker-compose-03.yml down -v
   ```
   - Stops and removes containers, images, and **volumes**.