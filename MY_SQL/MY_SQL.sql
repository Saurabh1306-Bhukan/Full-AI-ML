CREATE DATABASE IF NOT EXISTS instagram;

DROP DATABASE IF EXISTS instagram;

SHOW DATABASES;

USE instagram;

SHOW tables;

CREATE TABLE user (
id INT,
age INT,
name VARCHAR(50) NOT NULL,
email VARCHAR(50) UNIQUE,
follower INT DEFAULT 0,
following INT,
CONSTRAINT CHECK (age >= 13),
PRIMARY KEY (id)
);

INSERT INTO user
(id, age, name, email, follower, following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 123, 145),
(2, 15, "bob", "bob@gmail.com", 200, 200),
(3, 16, "casey", "casey@email.com", 300, 306),
(4, 17, "donald", "donald@gmail.com", 200, 105);

INSERT INTO user
(id, age, name, email, follower, following)
VALUES
(5, 14, "eve", "eve@yahoo.in", 400, 145),
(6, 16, "farah", "farah@gmail.com", 10000, 1000);


INSERT INTO user
(id, name, email, following)
VALUES
(7, "gimini", "gimini@yahoo.in", 120);


SELECT id, name, email FROM user;
SELECT * FROM user;
SELECT DISTINCT age FROM user;

--  WHERE Clause:- 
SELECT * FROM user
WHERE follower >= 200;

SELECT name, follower FROM user
WHERE follower >= 200;

SELECT name, age, follower FROM user
WHERE age BETWEEN 15 AND 17;

SELECT name, age, follower FROM user
WHERE age > 15 AND follower > 200;

SELECT name, follower, email FROM user
WHERE email IN ("donald@gmail.com","bob@gmail.com","abc@gmail.com");

SELECT name, age, email FROM user
WHERE age IN (14, 16);

SELECT name, age, email FROM user
WHERE age NOT IN (14, 16);


-- LIMIT Clause:- 

SELECT name, age, email FROM user
WHERE age > 14
LIMIT 2;

SELECT name, age, email FROM user
LIMIT 3;


-- ORDER BY Clause:- 

SELECT name, age, follower FROM user
ORDER BY follower ASC;      -- DESC



-- Aggregate Functions:- COUNT(), MAX(), MIN(), SUM(), AVG()


SELECT MAX(follower) FROM user;

SELECT COUNT(age) FROM user
WHERE age = 14;

SELECT MIN(age) FROM user;

SELECT AVG(age) FROM user;

SELECT SUM(follower) FROM user;


-- GROUP BY Clause:- 

SELECT COUNT(id) FROM user 
GROUP BY age;

SELECT age, COUNT(id) FROM user 
GROUP BY age;


-- HAVING Clause:- 

SELECT age, MAX(follower) FROM user 
GROUP BY age
HAVING MAX(follower) > 200;


-- General Order:-
    -- 1. SELECT column(s)
    -- 2. FROM table_name
    -- 3. WHERE condition
    -- 4. GROUP BY column(s)
    -- 5. HAVING condition
    -- 6. ORDER BY column(s) ASC;
    
SELECT age, MAX(follower) FROM user 
GROUP BY age
HAVING MAX(follower) > 200
ORDER BY age DESC;




CREATE TABLE post (
id INT PRIMARY KEY,
content VARCHAR(100),
user_id INT,
FOREIGN KEY (user_id) REFERENCES user(id)
);

INSERT INTO post
(id, content, user_id)
VALUES
(101, "Hello World", 3),
(102, "Bye Bye", 1),
(103, "Hello Delta", 3);


-- Table Queries:- 

-- UPDATE :-

UPDATE user
SET follower = 600
WHERE age = 16;

SELECT * FROM user;

SET SQL_SAFE_UPDATES = 0;

-- DELETE :-

DELETE FROM user
WHERE age = 14;

-- ALTER :- To change the schema

-- 1. ADD Column:- 

ALTER TABLE user
ADD COLUMN city VARCHAR(25) DEFAULT "Delhi";
 
 -- 2. DROP Column :-
 SELECT * FROM user;
 
 ALTER TABLE user
 DROP COLUMN age;
 
 -- 3. RENAME Table:- 
 
ALTER TABLE user
RENAME TO instaUser;
 
 SELECT * FROM instaUser;
 
ALTER TABLE instaUser
RENAME TO user;

SELECT * FROM user;
 
 -- 4. CHANGE Column (rename) :-
 
ALTER TABLE user
CHANGE COLUMN follower subscribers INT DEFAULT 0 ;

SELECT * FROM user;


-- 5. MODIFY Column (modify datatype/ constraint)

ALTER TABLE user
MODIFY subscribers INT DEFAULT 5;

SELECT * FROM user;


-- 6. TRUNCATE (To delete tables data)

TRUNCATE TABLE user;

SELECT * FROM user;



-- Practice Question :

CREATE DATABASE IF NOT EXISTS college;

USE college;

CREATE TABLE teacher (
id INT PRIMARY KEY,
name VARCHAR(50),
subject VARCHAR(50),
salary INT
);

INSERT INTO teacher 
(id, name, subject, salary)
VALUES
(23, "ajay", "math", 50000),
(47, "bharat", "english", 60000),
(18, "chetan", "chemistry", 45000),
(9, "divya", "physics", 75000);

SELECT * FROM teacher;


SELECT * FROM teacher
WHERE salary > 55000;

ALTER TABLE teacher
CHANGE COLUMN salary ctc INT;

UPDATE teacher
SET ctc = ctc + ctc * (0.25);

ALTER TABLE teacher
ADD COLUMN city VARCHAR(50) DEFAULT "Gurgaon";

ALTER TABLE teacher
DROP COLUMN ctc;


CREATE TABLE student (
roll_no INT PRIMARY  KEY,
name VARCHAR(50),
city VARCHAR(50),
marks INT
);

INSERT INTO student 
(roll_no, name, city, marks)
VALUES
(110, "adam", "Delhi", 76),
(108, "bob", "Mumbai", 65),
(124, "casey", "Pune", 94),
(112, "duke", "Pune", 80);

SELECT * FROM student;

SELECT * FROM student 
WHERE marks > 75;

SELECT DISTINCT city FROM student;

SELECT city
FROM student
GROUP BY city;

SELECT city, MAX(marks) 
FROM student
GROUP BY city;

SELECT AVG(marks) FROM student;

ALTER TABLE student
ADD COLUMN grade VARCHAR(5);

UPDATE student
SET grade  = "O"
WHERE marks >= 80;

UPDATE student
SET grade  = "A"
WHERE marks >= 70 AND marks < 80;

UPDATE student
SET grade  = "B"
WHERE marks >= 60 AND marks < 70;

