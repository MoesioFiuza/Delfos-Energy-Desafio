CREATE TABLE IF NOT EXISTS data (
    timestamp TIMESTAMP PRIMARY KEY,
    wind_speed FLOAT NOT NULL,
    power FLOAT NOT NULL,
    ambient_temperature FLOAT NOT NULL
);
