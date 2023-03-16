-- creating the table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);

-- creating these records
INSERT INTO second_table (id, name, score)
VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);