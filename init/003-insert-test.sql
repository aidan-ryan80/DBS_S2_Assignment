-- CREATE TRIGGER before_insert_check_valid_ski_pass
-- BEFORE INSERT ON reservation
-- FOR EACH ROW
-- BEGIN
--     DECLARE reservation_days INT;
--     DECLARE ski_pass_days INT;

--     IF NEW.packgeID IS NOT NULL THEN

--     SET reservation_days = DATEDIFF(NEW.checkOutDate, NEW.checkInDate)

--     SELECT CASE
--             WHEN sp.passType = 'Day Pass' THEN 1
--             WHEN sp.passType = '2 Day Pass' THEN 2
--             WHEN sp.passType = '3 Day Pass' THEN 3
--             WHEN sp.passType = '4 Day Pass' THEN 4
--             WHEN sp.passType = '5 Day Pass' THEN 5
--             WHEN sp.passType = '6 Day Pass' THEN 6
--             WHEN sp.passType = '7 Day Pass' THEN 7
--             ELSE 0
--         END INTO ski_pass_days
--     FROM skiPass sp
--     JOIN package p ON sp.skiPassID = p.skiPassID
--     WHERE p.packageID = NEW.packageID
--     LIMIT 1;

--     -- Check if ski pass exceeds reservation duration
--         IF ski_pass_days > reservation_days THEN
--             SIGNAL SQLSTATE '45000'
--             SET MESSAGE_TEXT = 'Ski pass duration exceeds reservation duration';
--         END IF;

--     END IF;
-- END$$

-- Could be used for the the reservation table:
-- startDate DATETIME NOT NULL,
-- endDate DATETIME NOT NULL,
-- validityPeriod INT AS (TIMESTAMPDIFF(DAY, startDate, endDate)) STORED,
-- CHECK (validityPeriod > 0),