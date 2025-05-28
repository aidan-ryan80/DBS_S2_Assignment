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

-- CREATE MATERIALIZED VIEW skipasses_by_minute WITH (timescaledb.continuous) AS SELECT time_bucket('1 minute', scan_time) AS bucket, rsp.passtype, rsp.skipassid, sr.name, sc.customerid,c.name,sc.reservationid, r.checkindate, r.checkoutdate FROM skipass_scans sc JOIN res_ski_passes rsp ON sc.res_skipass_id = rsp.id JOIN skiresorts sr ON sc.resortid = sr.resortid JOIN customers c ON sc.customerid = c.customerid JOIN reservations r ON sc.reservationid = r.reservationid GROUP BY bucket WITH NO DATA;