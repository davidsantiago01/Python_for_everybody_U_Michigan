
--Create SQL table
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
-- delete any rows and insert new rows
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Trafford', 28);
INSERT INTO Ages (name, age) VALUES ('Alessia', 31);
INSERT INTO Ages (name, age) VALUES ('Klaudia', 19);
INSERT INTO Ages (name, age) VALUES ('Johnpaul', 31);
INSERT INTO Ages (name, age) VALUES ('Maisey', 38);

-- run code belw
SELECT hex(name || age) AS X FROM Ages ORDER BY X

416C65737369613331
4A6F686E7061756C3331
4B6C61756469613139
4D61697365793338
54726166666F72643238
