DROP TABLE IF EXISTS breweries;

CREATE TABLE breweries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bid TEXT NOT NULL,
    name TEXT NOT NULL,
    brewery_type TEXT NOT NULL,
    street TEXT NULL,
    addr2 TEXT NULL,
    addr3 TEXT NULL,
    city TEXT NULL,
    state TEXT NULL,
    county_province TEXT NULL,
    postal_code TEXT NULL,
    country TEXT NULL,
    longitude TEXT NULL,
    latitude TEXT NULL,
    phone TEXT NULL,
    website_url TEXT NULL,
    updated_at TEXT NULL,
    created_at TEXT NULL
);