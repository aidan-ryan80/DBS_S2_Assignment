-- Inserting a single entry that must be unique into the hotel table
INSERT INTO hotel (address, name) VALUES ('myaddress123, 2001, Vienna', 'Awesome Resort');

-- Inserting at least 10 entries into the following tables
INSERT INTO customer (email, phoneNumber, name, age, address)
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
    ('daniel.anderson@example.com', '8899001122', 'Daniel Anderson', '31', '951 Spruce St');

INSERT INTO paymentInfo (customerID, billingAddress, cardHolderName, expirationDate, cardIssuer, cardNumber)
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
    (10, '951 Spruce St', 'Daniel Anderson', '2026-04-30', 'MasterCard', '5500000000007890');

INSERT INTO skiResort (name, size, location, difficultyLevel, skiLiftsCount, slopesCount, businessHours)
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

INSERT INTO skiPass (resortID, passType, price)
VALUES
-- Alpine Meadows (Intermediate)
(1, 'Day Pass', 55.00),
(1, '2 Day Pass', 105.00),
(1, '3 Day Pass', 150.00),
(1, '4 Day Pass', 190.00),
(1, '5 Day Pass', 225.00),
(1, '6 Day Pass', 255.00),
(1, '7 Day Pass', 280.00),

-- Snowbird (Advanced)
(2, 'Day Pass', 65.00),
(2, '2 Day Pass', 125.00),
(2, '3 Day Pass', 180.00),
(2, '4 Day Pass', 230.00),
(2, '5 Day Pass', 275.00),
(2, '6 Day Pass', 315.00),
(2, '7 Day Pass', 350.00),

-- Whistler Blackcomb (Expert, largest)
(3, 'Day Pass', 80.00),
(3, '2 Day Pass', 155.00),
(3, '3 Day Pass', 225.00),
(3, '4 Day Pass', 290.00),
(3, '5 Day Pass', 350.00),
(3, '6 Day Pass', 405.00),
(3, '7 Day Pass', 455.00),

-- Aspen Snowmass (Intermediate, large)
(4, 'Day Pass', 70.00),
(4, '2 Day Pass', 135.00),
(4, '3 Day Pass', 195.00),
(4, '4 Day Pass', 250.00),
(4, '5 Day Pass', 300.00),
(4, '6 Day Pass', 345.00),
(4, '7 Day Pass', 385.00),

-- Zermatt (Expert, very prestigious)
(5, 'Day Pass', 78.00),
(5, '2 Day Pass', 150.00),
(5, '3 Day Pass', 215.00),
(5, '4 Day Pass', 275.00),
(5, '5 Day Pass', 330.00),
(5, '6 Day Pass', 380.00),
(5, '7 Day Pass', 425.00),

-- Chamonix (Advanced, large)
(6, 'Day Pass', 75.00),
(6, '2 Day Pass', 145.00),
(6, '3 Day Pass', 210.00),
(6, '4 Day Pass', 270.00),
(6, '5 Day Pass', 325.00),
(6, '6 Day Pass', 375.00),
(6, '7 Day Pass', 420.00),

-- Cortina d'Ampezzo (Intermediate, smaller)
(7, 'Day Pass', 52.00),
(7, '2 Day Pass', 100.00),
(7, '3 Day Pass', 143.00),
(7, '4 Day Pass', 182.00),
(7, '5 Day Pass', 217.00),
(7, '6 Day Pass', 248.00),
(7, '7 Day Pass', 275.00),

-- Niseko (Beginner)
(8, 'Day Pass', 45.00),
(8, '2 Day Pass', 85.00),
(8, '3 Day Pass', 122.00),
(8, '4 Day Pass', 156.00),
(8, '5 Day Pass', 187.00),
(8, '6 Day Pass', 215.00),
(8, '7 Day Pass', 240.00),

-- Banff Sunshine (Advanced)
(9, 'Day Pass', 68.00),
(9, '2 Day Pass', 130.00),
(9, '3 Day Pass', 190.00),
(9, '4 Day Pass', 245.00),
(9, '5 Day Pass', 295.00),
(9, '6 Day Pass', 340.00),
(9, '7 Day Pass', 380.00),

-- St. Anton (Expert)
(10, 'Day Pass', 76.00),
(10, '2 Day Pass', 146.00),
(10, '3 Day Pass', 210.00),
(10, '4 Day Pass', 270.00),
(10, '5 Day Pass', 325.00),
(10, '6 Day Pass', 375.00),
(10, '7 Day Pass', 420.00);

INSERT INTO transport (resortID, type, price, timetable)
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

INSERT INTO room (roomNumber, price, type, availability) 
VALUES
-- Floor 1
(101, 100.00, 'single', 'available'),
(102, 120.00, 'double', 'available'),
(103, 130.00, 'triple', 'unavailable'),
-- Floor 2
(201, 150.00, 'single', 'available'),
(202, 180.00, 'double', 'available'),
(203, 200.00, 'triple', 'available'),
-- Floor 3
(301, 200.00, 'single', 'unavailable'),
(302, 220.00, 'double', 'available'),
(303, 250.00, 'quadruple', 'available'),
-- Floor 4
(401, 250.00, 'single', 'available'),
(402, 280.00, 'double', 'unavailable'),
(403, 300.00, 'triple', 'available'),
-- Floor 5
(501, 350.00, 'single', 'available'),
(502, 380.00, 'double', 'unavailable'),
(503, 400.00, 'quadruple', 'available');

-- Insert into package
INSERT INTO package (name, description, price, roomID, skiPassID) VALUES 
("Alpine Starter", "1 day access to Alpine Meadows with shuttle transport", NULL, 101, 1),
("Snowbird Explorer", "3-day pass at Snowbird with shuttle and snowmobile access", NULL, 103, 10),
("Whistler Elite", "Luxury heli tour with 2-day pass", NULL, 301, 16),
("Aspen Comfort", "Aspen access with 4-day ski pass and shuttle", NULL, 203, 25),
("Zermatt Prestige", "Train and snowmobile access to Zermatt with 5-day ski pass", NULL, 401, 33),
("Chamonix Ride", "Chamonix shuttle with 2-day ski pass", NULL, 202, 37),
("Cortina Deal", "Affordable access to Cortina with snowmobile and 3-day pass", NULL, 403, 44),
("Niseko Discover", "Train and shuttle to Niseko with 2-day pass", NULL, 502, 51),
("Banff Sunshine Pack", "Banff shuttle with 4-day pass", NULL, 503, 60),
("St. Anton Tour", "Train to St. Anton with 1-day ski pass", NULL, 302, 64);

-- Link packages with transport
INSERT INTO packageTransport (packageID, transportID) VALUES 
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

-- INSERT INTO table_name (column1, column2, column3)
-- VALUES 
--     (value1a, value2a, value3a),
--     (value1b, value2b, value3b),
--     (value1c, value2c, value3c);

-- INSERT INTO table_name (column1, column2, column3)
-- VALUES 
--     (value1a, value2a, value3a),
--     (value1b, value2b, value3b),
--     (value1c, value2c, value3c);