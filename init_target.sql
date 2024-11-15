CREATE TABLE IF NOT EXISTS signal (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS data (
    timestamp TIMESTAMP NOT NULL,
    signal_id INTEGER REFERENCES signal(id),
    value FLOAT NOT NULL,
    PRIMARY KEY (timestamp, signal_id)
);

