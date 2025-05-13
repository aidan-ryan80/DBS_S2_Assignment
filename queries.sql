-- Selecting all reservations that have been confirmed and payed:
SELECT * FROM Reservations R 
WHERE R.status = "confirmed" 
AND R.paymentStatus = "payed";

-- Selecting all customers that have not payed for their reservations yet in order to send Debt collectors after them:
SELECT C.customerID, C.email, C.phoneNumber, C.name, C.age, C.address FROM Customers C 
JOIN Reservations R ON R.customerID = C.CustomerID 
WHERE R.paymentStatus = "unpayed";

-- Querying for the total income our evil Ski Hotel Monopoly has made in the first quarter: 6560.00
SELECT SUM(R.totalCost) 
FROM Reservations R 
WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-01-01' AND '2025-03-31';

SELECT SUM(R.totalCost) 
FROM Reservations R 
WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-04-01' AND '2025-06-30'; -- Second Quarter Income: 4440.00

SELECT SUM(R.totalCost) 
FROM Reservations R 
WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-07-01' AND '2025-09-30'; -- Third Quarter Income: 2260.00

SELECT SUM(R.totalCost) 
FROM Reservations R 
WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-10-01' AND '2025-12-31'; -- Fourth Quarter Income: NULL

SELECT SUM(R.totalCost) 
FROM Reservations R 
WHERE R.paymentStatus = "payed" AND  checkInDate BETWEEN '2025-01-01' AND '2025-12-31'; -- Financial Year 2025 Income: 13266.00 

-- Total amount not payed yet for Reservations
SELECT SUM(R.totalCost) 
FROM Reservations R 
WHERE R.paymentStatus = "unpayed" OR R.paymentStatus = "failed"; -- 32374.00

-- List all customers who have booked a skipass as part of at least one of their future reservations, sorted by the (combined) number of nights of their reservations (descending).
SELECT r.status, r.checkInDate, r.checkOutDate, c.name, r.packageID 
FROM reservation r 
JOIN customer c ON r.customerID = c.customerID
WHERE r.status = 'confirmed' AND r.paymentStatus = 'payed'
ORDER BY DATEDIFF(r.checkOutDate, r.checkInDate) DESC;

-- Find the most often booked package.
SELECT p.packageID, p.name, 
COUNT(*) AS package_booking_count
FROM customer c
JOIN reservation r ON r.customerID = c.customerID
JOIN package p ON r.packageID = p.packageID
WHERE r.status != 'cancelled'
GROUP BY p.packageID
ORDER BY package_booking_count DESC
LIMIT 1;

-- Retrieve all reservations with a total price above a certain threshold.
SELECT r.reservationID, r.totalCost, r.status, r.paymentStatus, c.customerID, c.name
FROM customer c
JOIN reservation r ON r.customerID = c.customerID
WHERE r.totalCost > 1000;

-- Find the total revenue from package sales within a predefined date range.
SELECT SUM(package_prices) AS packages_total_revenue, SUM(reservations_total_costs) AS reservations_total_revenue
FROM (SELECT p.price AS package_prices, r.totalCost AS reservations_total_costs
FROM customer c
JOIN reservation r ON r.customerID = c.customerID
JOIN package p ON r.packageID = p.packageID
WHERE r.status != 'cancelled' AND r.checkInDate >= '2024-01-01' AND r.checkOutDate <= '2030-01-01') 
AS packages;

-- Query for testing purpose.
SELECT p.price, p.name, r.reservationID, c.name, c.customerID
FROM customer c
JOIN reservation r ON r.customerID = c.customerID
JOIN package p ON r.packageID = p.packageID
WHERE r.checkInDate >= '2024-01-01' AND r.checkOutDate <= '2030-01-01';

-- The most frequently used room vs the least frequently used room
SELECT * FROM (
SELECT rm.roomNumber, rm.floor, rm.type, rm.price,
COUNT(*) AS room_usage
FROM customer c
JOIN reservation r ON r.customerID = c.customerID
JOIN room rm ON r.roomID = rm.roomNumber
WHERE r.status = 'completed'
GROUP BY rm.roomNumber
ORDER BY room_usage DESC
LIMIT 1) AS most_frequently_used
JOIN 
(SELECT rm.roomNumber, rm.floor, rm.type, rm.price,
COUNT(*) AS room_usage
FROM customer c
JOIN reservation r ON r.customerID = c.customerID
JOIN room rm ON r.roomID = rm.roomNumber
WHERE r.status = 'completed'
GROUP BY rm.roomNumber
ORDER BY room_usage ASC
LIMIT 1) AS least_frequently_used;