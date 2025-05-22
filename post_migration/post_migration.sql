CREATE TABLE skipass_scans (
  scan_time     TIMESTAMPTZ     NOT NULL,
  skipassid    INT             NOT NULL,
  resortid  INT             NOT NULL,
  PRIMARY KEY (scan_time, skipassid),
  CONSTRAINT fk_skipass FOREIGN KEY (skipassid) REFERENCES skipasses(skipassid),
  CONSTRAINT fk_skiresort FOREIGN KEY (resortid) REFERENCES skiresorts(resortid)
);

SELECT create_hypertable('skipass_scans', 'scan_time');