CREATE TABLE IF NOT EXISTS dados (
    timestamp TIMESTAMP PRIMARY KEY,
    velocidade_vento FLOAT NOT NULL,
    potencia FLOAT NOT NULL,
    temperatura_ambiente FLOAT NOT NULL
);
