-- creates the db hbtn_0d_usa
-- creates the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE PRIMARY KEY ,
    name VARCHAR(256) NOT NULL
);
