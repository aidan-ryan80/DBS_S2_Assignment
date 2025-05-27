CREATE TABLE skipass_scans (
  scanid SERIAL, 
  scan_time TIMESTAMPTZ NOT NULL, 
  skipassid INT NOT NULL, 
  resortid INT NOT NULL, 
  customerid INT NOT NULL, 
  reservationid INT NOT NULL, 
PRIMARY KEY (scanid), 
CONSTRAINT fk_skipass FOREIGN KEY (skipassid) REFERENCES skipasses(skipassid), 
CONSTRAINT fk_resort FOREIGN KEY (resortid) REFERENCES skiresorts(resortid), 
CONSTRAINT fk_customer FOREIGN KEY (customerid) REFERENCES customers(customerid), 
CONSTRAINT fk_reservation FOREIGN KEY (reservationid) REFERENCES reservations(reservationid));

SELECT create_hypertable('skipass_scans', 'scan_time');