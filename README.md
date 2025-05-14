# DBS_S2_Assignment
##### Database Systems Assignment for Semester 2 of the IMC Bachelor’s Program in Computer Science

## 📌 Introduction
This assignment involves developing a **MariaDB database** for a hotel that specializes in customers on skiing trips. An **Entity Relationship Diagram (ERD)** was designed beforehand and is included in this repository. Note: the ERD does not include two entities that were later added during database implementation.

---

## 🛠️ How to Initialize the Database

### Method 1: Using `docker-compose`
1. Navigate to the project root directory:  
   ```bash
   cd DBS_S2_Assignment
   ```
2. Run the containers:  
   ```bash
   docker-compose up -d
   ```
   - This uses the MariaDB 10.3 image and initializes the database using the `.sql` files in the `init/` directory (executed in alphabetical order).
3. To enter the MariaDB shell:  
   ```bash
   docker exec -it <container-name> mysql -u root -p
   ```
   - Password: `rootpass` (defined in `docker-compose.yml`)
   - The `SkiHotelDB` database will already exist and be accessible.
4. Python scripts included in the repo:
   - `ski_hotel_init.py`: creates all tables and inserts initial data.
   - `ski_hotel_queries.py`: sample queries for testing the database.
   - `ski_hotel_delete_data.py`: truncates all tables.
   - `ski_hotel_reset.py`: drops all tables.
5. To stop and clean up:
   ```bash
   docker-compose down -v
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
6. Use the same Python scripts listed in Method 1 for testing, resetting, and developing.
7. To stop and clean up manually:
   ```bash
   docker stop <container-name>
   docker rm <container-name>
   docker image rm <image-name>
   docker volume prune
   ```

---

## 📦 Python Dependencies

Before running any Python scripts, install the required packages:

```bash
pip install mariadb
pip install tabulate
```

These are needed for:
- Connecting to the MariaDB database (`mariadb`)
- Displaying query results in table format (`tabulate`)

---

## ▶️ Running Python Scripts

To execute any of the included Python files, use the following command format:

```bash
python filename.py
```

Examples:
```bash
python execute_queries.py
python ski_hotel_init.py
python ski_hotel_delete_data.py
python ski_hotel_reset.py
```

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
