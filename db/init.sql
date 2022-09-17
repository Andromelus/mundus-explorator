CREATE TABLE user (
    id               INTEGER  PRIMARY KEY AUTOINCREMENT,
    name             STRING   NOT NULL,
    password         STRING   NOT NULL
                              UNIQUE,
    token            STRING,
    token_expires_at DATETIME
);
