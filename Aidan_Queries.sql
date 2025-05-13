-- Selecting all reservations that have been confirmed and payed:
SELECT * FROM Reservations R 
WHERE R.status = "confirmed" 
AND R.paymentStatus = "payed";

-- Selecting all customers that have not payed for their reservations yet in order to send Debt collectors after them:
SELECT C.customerID, C.email, C.phoneNumber, C.name, C.age, C.address FROM Customers C 
JOIN Reservations R ON R.customerID = C.CustomerID 
WHERE R.paymentStatus = "unpayed";

-- Querying for the total income our evil Ski Hotel Monopoly has made in the first quarter: 6560.00
SELECT SUM(R.totalCost) FROM Reservations R WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-01-01' AND '2025-03-31';
SELECT SUM(R.totalCost) FROM Reservations R WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-04-01' AND '2025-06-30'; -- Second Quarter Income: 4440.00
SELECT SUM(R.totalCost) FROM Reservations R WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-07-01' AND '2025-09-30'; -- Third Quarter Income: 2260.00
SELECT SUM(R.totalCost) FROM Reservations R WHERE R.paymentStatus = "payed" AND checkInDate BETWEEN '2025-10-01' AND '2025-12-31'; -- Fourth Quarter Income: NULL
SELECT SUM(R.totalCost) FROM Reservations R WHERE R.paymentStatus = "payed" AND  checkInDate BETWEEN '2025-01-01' AND '2025-12-31'; -- Financial Year 2025 Income: 13266.00 

-- Total amount not payed yet for Reservations
SELECT SUM(R.totalCost) FROM Reservations R WHERE R.paymentStatus = "unpayed" OR R.paymentStatus = "failed"; -- 32374.00