CREATE TABLE IF NOT EXISTS scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_type TEXT NOT NULL,
    network TEXT NOT NULL,
    start_time TEXT,
    end_time TEXT,
    status TEXT
);

CREATE TABLE IF NOT EXISTS hosts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_id INTEGER,
    ip TEXT NOT NULL,
    hostname TEXT,
    status TEXT,
    FOREIGN KEY(scan_id) REFERENCES scans(id)
);
