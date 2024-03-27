-- create db, table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  state_id INT FOREIGN KEY REFERENCES states(state_id),
  name VARCHAR(256)
);
