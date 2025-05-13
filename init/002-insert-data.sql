-- Inserting a single entry that must be unique into the hotel table
INSERT INTO Hotel (address, name) VALUES ('myaddress123, 2001, Vienna', 'Awesome Resort');

-- Inserting at least 10 entries into the following tables
INSERT INTO Customers (email, phoneNumber, name, age, address)
VALUES
    ('john.doe@example.com', '1234567890', 'John Doe', '30', '123 Main St'),
    ('jane.smith@example.com', '0987654321', 'Jane Smith', '25', '456 Elm St'),
    ('alice.brown@example.com', '1122334455', 'Alice Brown', '28', '789 Oak St'),
    ('michael.johnson@example.com', '2233445566', 'Michael Johnson', '35', '321 Pine St'),
    ('emily.davis@example.com', '3344556677', 'Emily Davis', '27', '654 Maple St'),
    ('david.wilson@example.com', '4455667788', 'David Wilson', '40', '987 Birch St'),
    ('sarah.miller@example.com', '5566778899', 'Sarah Miller', '22', '159 Cedar St'),
    ('chris.moore@example.com', '6677889900', 'Chris Moore', '33', '753 Walnut St'),
    ('laura.taylor@example.com', '7788990011', 'Laura Taylor', '29', '852 Chestnut St'),
    ('daniel.anderson@example.com', '8899001122', 'Daniel Anderson', '31', '951 Spruce St'),
    ('oliver.james@example.com', '9001122334', 'Oliver James', '26', '101 Birchwood Ave'),
    ('emma.watson@example.com', '9112233445', 'Emma Watson', '24', '202 Maplewood St'),
    ('liam.jones@example.com', '9223344556', 'Liam Jones', '32', '303 Cedarwood Dr'),
    ('sophia.brown@example.com', '9334455667', 'Sophia Brown', '30', '404 Pinewood Ln'),
    ('noah.davis@example.com', '9445566778', 'Noah Davis', '28', '505 Oakwood Ct'),
    ('ava.martin@example.com', '9556677889', 'Ava Martin', '27', '606 Elmwood Rd'),
    ('william.moore@example.com', '9667788990', 'William Moore', '34', '707 Walnut St'),
    ('mia.taylor@example.com', '9778899001', 'Mia Taylor', '23', '808 Chestnut Blvd'),
    ('james.anderson@example.com', '9889900112', 'James Anderson', '29', '909 Spruce Ave'),
    ('isabella.thomas@example.com', '9990011223', 'Isabella Thomas', '31', '1001 Redwood Dr'),
    ('lucas.jackson@example.com', '1001122334', 'Lucas Jackson', '36', '1102 Cypress Ln'),
    ('amelia.white@example.com', '1012233445', 'Amelia White', '25', '1203 Willow St'),
    ('elijah.harris@example.com', '1023344556', 'Elijah Harris', '33', '1304 Aspen Ct'),
    ('harper.clark@example.com', '1034455667', 'Harper Clark', '22', '1405 Magnolia Rd'),
    ('mason.lewis@example.com', '1045566778', 'Mason Lewis', '37', '1506 Sycamore Blvd'),
    ('ella.robinson@example.com', '1056677889', 'Ella Robinson', '26', '1607 Poplar Ave'),
    ('logan.walker@example.com', '1067788990', 'Logan Walker', '30', '1708 Birchwood Dr'),
    ('scarlett.young@example.com', '1078899001', 'Scarlett Young', '28', '1809 Maplewood Ln'),
    ('ethan.king@example.com', '1089900112', 'Ethan King', '35', '1901 Cedarwood Ct'),
    ('grace.hall@example.com', '1090011223', 'Grace Hall', '24', '2002 Pinewood St');

INSERT INTO PaymentInfos (customerID, billingAddress, cardHolderName, expirationDate, cardIssuer, cardNumber)
VALUES
    (1, '123 Main St', 'John Doe', '2025-12-31', 'Visa', '4111111111111111'),
    (2, '456 Elm St', 'Jane Smith', '2026-06-30', 'MasterCard', '5500000000000004'),
    (3, '789 Oak St', 'Alice Brown', '2024-09-15', 'American Express', '340000000000009'),
    (4, '321 Pine St', 'Michael Johnson', '2027-03-20', 'Discover', '6011000000000004'),
    (5, '654 Maple St', 'Emily Davis', '2025-11-10', 'Visa', '4111111111111234'),
    (6, '987 Birch St', 'David Wilson', '2026-01-25', 'MasterCard', '5500000000005678'),
    (7, '159 Cedar St', 'Sarah Miller', '2024-07-05', 'American Express', '340000000000567'),
    (8, '753 Walnut St', 'Chris Moore', '2027-02-14', 'Discover', '6011000000007890'),
    (9, '852 Chestnut St', 'Laura Taylor', '2025-08-19', 'Visa', '4111111111113456'),
    (10, '951 Spruce St', 'Daniel Anderson', '2026-04-30', 'MasterCard', '5500000000007890'),
    (11, '101 Birchwood Ave', 'Oliver James', '2026-12-31', 'Visa', '4111111111112222'),
    (12, '202 Maplewood St', 'Emma Watson', '2027-06-30', 'MasterCard', '5500000000003333'),
    (13, '303 Cedarwood Dr', 'Liam Jones', '2025-09-15', 'American Express', '340000000000444'),
    (14, '404 Pinewood Ln', 'Sophia Brown', '2028-03-20', 'Discover', '6011000000005555'),
    (15, '505 Oakwood Ct', 'Noah Davis', '2026-11-10', 'Visa', '4111111111116666'),
    (16, '606 Elmwood Rd', 'Ava Martin', '2027-01-25', 'MasterCard', '5500000000007777'),
    (17, '707 Walnut St', 'William Moore', '2025-07-05', 'American Express', '340000000000888'),
    (18, '808 Chestnut Blvd', 'Mia Taylor', '2028-02-14', 'Discover', '6011000000009999'),
    (19, '909 Spruce Ave', 'James Anderson', '2026-08-19', 'Visa', '4111111111110000'),
    (20, '1001 Redwood Dr', 'Isabella Thomas', '2027-04-30', 'MasterCard', '5500000000001111'),
    (21, '1102 Cypress Ln', 'Lucas Jackson', '2026-12-31', 'Visa', '4111111111113333'),
    (22, '1203 Willow St', 'Amelia White', '2027-06-30', 'MasterCard', '5500000000004444'),
    (23, '1304 Aspen Ct', 'Elijah Harris', '2025-09-15', 'American Express', '340000000000555'),
    (24, '1405 Magnolia Rd', 'Harper Clark', '2028-03-20', 'Discover', '6011000000006666'),
    (25, '1506 Sycamore Blvd', 'Mason Lewis', '2026-11-10', 'Visa', '4111111111117777'),
    (26, '1607 Poplar Ave', 'Ella Robinson', '2027-01-25', 'MasterCard', '5500000000008888'),
    (27, '1708 Birchwood Dr', 'Logan Walker', '2025-07-05', 'American Express', '340000000000999'),
    (28, '1809 Maplewood Ln', 'Scarlett Young', '2028-02-14', 'Discover', '6011000000000000'),
    (29, '1901 Cedarwood Ct', 'Ethan King', '2026-08-19', 'Visa', '4111111111115555'),
    (30, '2002 Pinewood St', 'Grace Hall', '2027-04-30', 'MasterCard', '5500000000002222');

INSERT INTO SkiResorts (name, size, location, difficultyLevel, skiLiftsCount, slopesCount, businessHours)
VALUES 
    ("Alpine Meadows", 45.50, "California, USA", "Intermediate", 13, 60, "Monday-Sunday: 08:00 - 17:00"),
    ("Snowbird", 50.75, "Utah, USA", "Advanced", 15, 85, "Monday-Sunday: 08:00 - 17:00"),
    ("Whistler Blackcomb", 82.30, "British Columbia, Canada", "Expert", 25, 200, "Monday-Sunday: 08:00 - 17:00"),
    ("Aspen Snowmass", 55.20, "Colorado, USA", "Intermediate", 21, 96, "Monday-Sunday: 08:00 - 17:00"),
    ("Zermatt", 70.00, "Valais, Switzerland", "Expert", 18, 150, "Monday-Sunday: 08:00 - 17:00"),
    ("Chamonix", 65.40, "Haute-Savoie, France", "Advanced", 20, 120, "Monday-Sunday: 08:00 - 17:00"),
    ("Cortina d'Ampezzo", 40.25, "Veneto, Italy", "Intermediate", 12, 50, "Monday-Sunday: 08:00 - 17:00"),
    ("Niseko", 38.10, "Hokkaido, Japan", "Beginner", 10, 40, "Monday-Sunday: 08:00 - 17:00"),
    ("Banff Sunshine", 48.60, "Alberta, Canada", "Advanced", 14, 75, "Monday-Sunday: 08:00 - 17:00"),
    ("St. Anton", 60.80, "Tyrol, Austria", "Expert", 22, 140, "Monday-Sunday: 08:00 - 17:00");

INSERT INTO SkiPasses (resortID, passType, price)
VALUES
-- Alpine Meadows (Intermediate)
(1, 'Day Pass', 55.00),
(1, '2 Day Pass', 105.00),
(1, '3 Day Pass', 150.00),
(1, '4 Day Pass', 190.00),
(1, '5 Day Pass', 225.00),
(1, '6 Day Pass', 255.00),
(1, '7 Day Pass', 280.00), -- 7

-- Snowbird (Advanced)
(2, 'Day Pass', 65.00),
(2, '2 Day Pass', 125.00),
(2, '3 Day Pass', 180.00), -- 10
(2, '4 Day Pass', 230.00),
(2, '5 Day Pass', 275.00),
(2, '6 Day Pass', 315.00),
(2, '7 Day Pass', 350.00), -- 14

-- Whistler Blackcomb (Expert, largest)
(3, 'Day Pass', 80.00),
(3, '2 Day Pass', 155.00), -- 16
(3, '3 Day Pass', 225.00),
(3, '4 Day Pass', 290.00),
(3, '5 Day Pass', 350.00),
(3, '6 Day Pass', 405.00),
(3, '7 Day Pass', 455.00),-- 21

-- Aspen Snowmass (Intermediate, large)
(4, 'Day Pass', 70.00),
(4, '2 Day Pass', 135.00),
(4, '3 Day Pass', 195.00),
(4, '4 Day Pass', 250.00), -- 25
(4, '5 Day Pass', 300.00),
(4, '6 Day Pass', 345.00),
(4, '7 Day Pass', 385.00), -- 28

-- Zermatt (Expert, very prestigious)
(5, 'Day Pass', 78.00),
(5, '2 Day Pass', 150.00),
(5, '3 Day Pass', 215.00),
(5, '4 Day Pass', 275.00),
(5, '5 Day Pass', 330.00), -- 33
(5, '6 Day Pass', 380.00),
(5, '7 Day Pass', 425.00), -- 35

-- Chamonix (Advanced, large)
(6, 'Day Pass', 75.00),
(6, '2 Day Pass', 145.00),
(6, '3 Day Pass', 210.00),
(6, '4 Day Pass', 270.00),
(6, '5 Day Pass', 325.00),
(6, '6 Day Pass', 375.00),
(6, '7 Day Pass', 420.00), -- 42

-- Cortina d'Ampezzo (Intermediate, smaller)
(7, 'Day Pass', 52.00),
(7, '2 Day Pass', 100.00),
(7, '3 Day Pass', 143.00),
(7, '4 Day Pass', 182.00),
(7, '5 Day Pass', 217.00),
(7, '6 Day Pass', 248.00),
(7, '7 Day Pass', 275.00), -- 49

-- Niseko (Beginner)
(8, 'Day Pass', 45.00),
(8, '2 Day Pass', 85.00),
(8, '3 Day Pass', 122.00),
(8, '4 Day Pass', 156.00),
(8, '5 Day Pass', 187.00),
(8, '6 Day Pass', 215.00),
(8, '7 Day Pass', 240.00), -- 56

-- Banff Sunshine (Advanced)
(9, 'Day Pass', 68.00),
(9, '2 Day Pass', 130.00),
(9, '3 Day Pass', 190.00),
(9, '4 Day Pass', 245.00),
(9, '5 Day Pass', 295.00),
(9, '6 Day Pass', 340.00),
(9, '7 Day Pass', 380.00), -- 63

-- St. Anton (Expert)
(10, 'Day Pass', 76.00),
(10, '2 Day Pass', 146.00),
(10, '3 Day Pass', 210.00),
(10, '4 Day Pass', 270.00),
(10, '5 Day Pass', 325.00),
(10, '6 Day Pass', 375.00),
(10, '7 Day Pass', 420.00); -- 70

INSERT INTO Transports (resortID, type, price, timetable)
VALUES
-- Alpine Meadows (resortID = 1)
(1, 'shuttle', 30.00, 'Shuttle departs every hour from 7 AM to 9 PM'),
-- Snowbird (resortID = 2)
(2, 'shuttle', 25.00, 'Shuttle departs every 30 minutes from 6:30 AM to 10 PM'),
(2, 'snowmobile', 150.00, 'Snowmobile transport for off-piste areas, available 24/7'),
-- Whistler Blackcomb (resortID = 3)
(3, 'helicopter', 500.00, 'Helicopter service, available on request for private tours'),
(3, 'shuttle', 40.00, 'Shuttle departs every 45 minutes from 7 AM to 9 PM'),
-- Aspen Snowmass (resortID = 4)
(4, 'helicopter', 600.00, 'Helicopter departs from private heliport, available daily'),
(4, 'shuttle', 35.00, 'Shuttle service from Aspen to Snowmass every 30 minutes'),
-- Zermatt (resortID = 5)
(5, 'train', 60.00, 'Train departs every hour from Visp station to Zermatt station'),
(5, 'snowmobile', 100.00, 'Snowmobile transport to remote slopes, available 24/7'),
-- Chamonix (resortID = 6)
(6, 'shuttle', 28.00, 'Shuttle departs every 30 minutes from 6:00 AM to 10:00 PM'),
-- Cortina d'Ampezzo (resortID = 7)
(7, 'shuttle', 20.00, 'Shuttle service available every hour from 8 AM to 6 PM'),
(7, 'snowmobile', 120.00, 'Snowmobile transport for off-road areas, available on request'),
-- Niseko (resortID = 8)
(8, 'train', 40.00, 'Train departs every 45 minutes from Sapporo to Niseko station'),
(8, 'shuttle', 25.00, 'Shuttle departs every 20 minutes from 7 AM to 9 PM'),
-- Banff Sunshine (resortID = 9)
(9, 'shuttle', 35.00, 'Shuttle departs every hour from Banff town center to the resort'),
(9, 'snowmobile', 150.00, 'Snowmobile transport available for remote areas'),
-- St. Anton (resortID = 10)
(10, 'shuttle', 32.00, 'Shuttle departs every 45 minutes from 6 AM to 8 PM'),
(10, 'train', 55.00, 'Train service available every 30 minutes from St. Anton Bahnhof');

INSERT INTO Rooms (roomNumber, price, type, availability) 
VALUES
-- Floor 1
(101, 100.00, 'single', 'available'),
(102, 120.00, 'double', 'available'),
(103, 130.00, 'triple', 'unavailable'),
(104, 140.00, 'quadruple', 'available'), -- New room
(105, 150.00, 'single', 'available'),    -- New room
-- Floor 2
(201, 150.00, 'single', 'available'),
(202, 180.00, 'double', 'available'),
(203, 200.00, 'triple', 'available'),
(204, 220.00, 'quadruple', 'available'), -- New room
(205, 240.00, 'single', 'available'),    -- New room
-- Floor 3
(301, 200.00, 'single', 'unavailable'),
(302, 220.00, 'double', 'available'),
(303, 250.00, 'quadruple', 'available'),
(304, 270.00, 'triple', 'available'),    -- New room
(305, 290.00, 'single', 'available'),    -- New room
-- Floor 4
(401, 250.00, 'single', 'available'),
(402, 280.00, 'double', 'unavailable'),
(403, 300.00, 'triple', 'available'),
(404, 320.00, 'quadruple', 'available'), -- New room
(405, 340.00, 'single', 'available'),    -- New room
-- Floor 5
(501, 350.00, 'single', 'available'),
(502, 380.00, 'double', 'unavailable'),
(503, 400.00, 'quadruple', 'available'),
(504, 420.00, 'triple', 'available'),    -- New room
(505, 440.00, 'single', 'available');    -- New room

-- Insert into package
INSERT INTO Packages (name, description, price, roomID, skiPassID) 
VALUES 
("Alpine Starter", "1 day access to Alpine Meadows with shuttle transport", NULL, 101, 1), -- single room, 1 day pass
("Snowbird Explorer", "3-day pass at Snowbird with shuttle and snowmobile access", NULL, 103, 10), -- triple room, 3 day pass
("Whistler Elite", "Luxury heli tour with 2-day pass", NULL, 301, 16), -- single room, 2 day pass
("Aspen Comfort", "Aspen access with 4-day ski pass and shuttle", NULL, 203, 25), -- triple room, 4 day pass
("Zermatt Prestige", "Train and snowmobile access to Zermatt with 5-day ski pass", NULL, 401, 33), -- single room, 5 day pass
("Chamonix Ride", "Chamonix shuttle with 2-day ski pass", NULL, 202, 37), -- double room
("Cortina Deal", "Affordable access to Cortina with snowmobile and 3-day pass", NULL, 403, 45), -- triple room
("Niseko Discover", "Train and shuttle to Niseko with 2-day pass", NULL, 502, 51), -- double room
("Banff Sunshine Pack", "Banff shuttle with 4-day pass", NULL, 503, 60), -- quadruple room
("St. Anton Tour", "Train to St. Anton with 1-day ski pass", NULL, 302, 64); -- double room

-- Link packages with transport
INSERT INTO PackagesTransports (packageID, transportID) 
VALUES 
(1, 1),
(2, 2),
(2, 3),
(3, 4),
(4, 6),
(5, 8),
(5, 9),
(6, 10),
(7, 12),
(8, 14),
(8, 15),
(9, 16),
(10, 18);

INSERT INTO Reservations (status, paymentStatus, checkInDate, checkOutDate, totalCost, hotelID, customerID, packageID, roomID)
VALUES 
    ('pending', 'unpayed', '2025-06-10', '2025-06-12', NULL, 1, 6, 1, 101), -- 2 days, packageID = 1 (1-day ski pass)
    ('pending', 'unpayed', '2025-07-01', '2025-07-05', NULL, 1, 7, 6, 202), -- 4 days, packageID = 6 (2-day ski pass)
    ('confirmed', 'unpayed', '2025-08-10', '2025-08-13', NULL, 1, 8, 7, 403), -- 3 days, packageID = 7 (3-day ski pass)
    ('completed', 'failed', '2025-10-05', '2025-10-09', NULL, 1, 9, 8, 502), -- 4 days, packageID = 8 (4-day ski pass)
    ('cancelled', 'unpayed', '2025-10-01', '2025-10-06', NULL, 1, 10, 9, 503), -- 5 days, packageID = 9 (4-day ski pass)
    ('confirmed', 'payed', '2025-01-10', '2025-01-14', NULL, 1, 11, 9, 503), -- 4 days, packageID = 9 (4-day ski pass)
    ('pending', 'unpayed', '2025-02-05', '2025-02-09', NULL, 1, 12, NULL, 102), -- 4 days, no package
    ('cancelled', 'unpayed', '2025-03-01', '2025-03-04', NULL, 1, 13, NULL, 103), -- 3 days, no package
    ('completed', 'payed', '2025-04-10', '2025-04-12', NULL, 1, 14, NULL, 104), -- 2 days, no package
    ('no_show', 'unpayed', '2025-05-01', '2025-05-06', NULL, 1, 15, NULL, 105), -- 5 days, no package
    ('confirmed', 'payed', '2025-06-15', '2025-06-18', NULL, 1, 16, 6, 202), -- 3 days, packageID = 6 (2-day ski pass)
    ('pending', 'unpayed', '2025-07-10', '2025-07-14', NULL, 1, 17, 7, 403), -- 4 days, packageID = 7 (3-day ski pass)
    ('cancelled', 'unpayed', '2025-07-05', '2025-07-09', NULL, 1, 18, NULL, 203), -- 4 days, no package
    ('completed', 'payed', '2025-02-05', '2025-02-08', NULL, 1, 24, 8, 502), -- 3 days, packageID = 8 (2-day ski pass)
    ('no_show', 'unpayed', '2025-04-01', '2025-04-04', NULL, 1, 25, NULL, 305), -- 3 days, no package
    ('pending', 'unpayed', '2025-04-10', '2025-04-13', NULL, 1, 26, 9, 503), -- 3 days, packageID = 9 (4-day ski pass)
    ('cancelled', 'unpayed', '2025-06-01', '2025-06-05', NULL, 1, 27, NULL, 403), -- 4 days, no package
    ('completed', 'payed', '2025-05-10', '2025-05-14', NULL, 1, 28, 10, 302), -- 4 days, packageID = 10 (1-day ski pass)
    ('no_show', 'unpayed', '2025-06-01', '2025-06-05', NULL, 1, 29, NULL, 405), -- 4 days, no package
    ('confirmed', 'payed', '2025-05-01', '2025-05-06', NULL, 1, 30, 2, 103), -- 5 days, packageID = 2 (3-day ski pass)
    ('pending', 'unpayed', '2025-07-01', '2025-07-03', NULL, 1, 6, 1, 101), -- 2 days, packageID = 1 (1-day ski pass)
    ('pending', 'unpayed', '2025-08-01', '2025-08-06', NULL, 1, 7, 3, 301), -- 5 days, packageID = 3 (2-day ski pass)
    ('confirmed', 'unpayed', '2025-09-01', '2025-09-03', NULL, 1, 8, 4, 203), -- 2 days, packageID = 4 (4-day ski pass)
    ('completed', 'failed', '2025-10-05', '2025-10-10', NULL, 1, 9, 5, 401), -- 5 days, packageID = 5 (5-day ski pass)
    ('cancelled', 'unpayed', '2025-11-01', '2025-11-05', NULL, 1, 10, 4, 203), -- 4 days, packageID = 4 (4-day ski pass)
    ('confirmed', 'payed', '2025-02-05', '2025-02-09', NULL, 1, 11, 9, 503), -- 4 days, packageID = 9 (4-day ski pass)
    ('pending', 'unpayed', '2025-03-05', '2025-03-09', NULL, 1, 12, NULL, 102), -- 4 days, no package
    ('cancelled', 'unpayed', '2025-04-01', '2025-04-04', NULL, 1, 13, NULL, 103), -- 3 days, no package
    ('completed', 'payed', '2025-05-05', '2025-05-08', NULL, 1, 14, NULL, 104), -- 3 days, no package
    ('no_show', 'unpayed', '2025-06-01', '2025-06-06', NULL, 1, 15, NULL, 105), -- 5 days, no package
    ('confirmed', 'payed', '2025-07-01', '2025-07-04', NULL, 1, 16, 3, 301), -- 3 days, packageID = 3 (2-day ski pass)
    ('pending', 'unpayed', '2025-08-05', '2025-08-10', NULL, 1, 17, 4, 203), -- 5 days, packageID = 4 (4-day ski pass)
    ('cancelled', 'unpayed', '2025-09-05', '2025-09-10', NULL, 1, 18, NULL, 203), -- 5 days, no package
    ('completed', 'payed', '2025-02-05', '2025-02-08', NULL, 1, 24, 8, 502), -- 3 days, packageID = 8 (2-day ski pass)
    ('no_show', 'unpayed', '2025-03-01', '2025-03-05', NULL, 1, 25, NULL, 305), -- 4 days, no package
    ('pending', 'unpayed', '2025-04-05', '2025-04-09', NULL, 1, 26, 9, 503), -- 4 days, packageID = 9 (4-day ski pass)
    ('cancelled', 'unpayed', '2025-05-01', '2025-05-06', NULL, 1, 27, NULL, 403), -- 5 days, no package
    ('completed', 'payed', '2025-06-15', '2025-06-19', NULL, 1, 28, 10, 302), -- 4 days, packageID = 10 (1-day ski pass)
    ('no_show', 'unpayed', '2025-07-01', '2025-07-05', NULL, 1, 29, NULL, 405), -- 4 days, no package
    ('confirmed', 'payed', '2025-08-01', '2025-08-05', NULL, 1, 30, 10, 302); -- 5 days, packageID = 10 (1-day ski pass)

    COMMIT;