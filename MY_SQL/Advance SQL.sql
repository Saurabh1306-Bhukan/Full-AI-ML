-- Transactions:-
     -- Disable autocommit :- SET autocommit = 0;
     
SELECT @@autocommit;

SET autocommit = 0;

     -- Enable autocommit :-  SET autocommit = 1;
     
SET autocommit = 1;
     
	
-- ----------------------------------------------------------------------------


CREATE DATABASE IF NOT EXISTS prime;

USE prime;

CREATE TABLE accounts (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
balance DECIMAL(10, 2)
);

INSERT INTO accounts 
(name, balance)
VALUES
('Adam', 500.00),
('Bob', 300.00),
('Charlie', 1000.00);


SELECT * FROM accounts;


-- Start & Commit
-- Transaction

START TRANSACTION;

UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;

COMMIT;

SELECT * FROM accounts;


-- Rollback :- 

START TRANSACTION;

UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;

ROLLBACK;

SELECT * FROM accounts;


-- Savepoint :-

START TRANSACTION;

UPDATE accounts SET balance = balance + 1000 WHERE id = 1;
SAVEPOINT  after_wallet_topup;

UPDATE accounts SET balance = balance + 10 WHERE id = 2;

ROLLBACK TO after_walet_topup;
COMMIT;

-- -------------------------------------------------------------------

CREATE TABLE customers (
customer_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO customers 
VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');


CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
amount INT
);

INSERT INTO orders
VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);


SELECT * FROM customers;
SELECT * FROM orders;

-- JOINs :- Inner Join,  Left Join,  Right Join,  Full Join,  Outer Join,  Cross Join,  Self Join

-- INNER JOIN :-

SELECT *                      -- we can check specific column : c.customer_id, o.order_id, c.name
FROM customers c
INNER JOIN orders o 
ON c.customer_id = o.customer_id;


-- LEFT JOIN :-

SELECT *                     
FROM customers c
LEFT JOIN orders o 
ON c.customer_id = o.customer_id;

 

-- RIGHT JOIN :-

SELECT *                     
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id = o.customer_id;



-- OUTER JOIN :- 

SELECT *                     
FROM customers c
LEFT JOIN orders o 
ON c.customer_id = o.customer_id
UNION
SELECT *                     
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id = o.customer_id;



-- CROSS JOIN :-

SELECT * 
FROM customers
CROSS JOIN orders;


-- SELF JOIN :-

SELECT * 
FROM customers as A
JOIN customers as B
ON A.customer_id = B.customer_id;


-- LEFT EXCLUSIVE JOIN :-

SELECT * 
FROM customers as A
LEFT JOIN orders as B
ON A.customer_id = B.customer_id
WHERE B.customer_id IS NULL;


-- RIGHT EXCLUSIVE JOIN :- 

SELECT * 
FROM customers as A
RIGHT JOIN orders as B
ON A.customer_id = B.customer_id
WHERE A.customer_id IS NULL;



-- Sub-Queries :- 

SELECT * 
FROM orders
WHERE amount > (
    SELECT AVG(amount)
    FROM orders      
);

-- SUB-Querie with SELECT

SELECT name,
       (
          SELECT COUNT(*)
          FROM orders o
          WHERE o.customer_id = c.customer_id
       ) AS order_count
FROM customers c;


-- inside FROM

SELECT 
     summary.customer_id, 
     summary.avg_amount
FROM 
    (
       SELECT customer_id,
       AVG(amount) as avg_amount
    FROM orders
    GROUP BY customer_id
    ) as summary;
    
    
-- VIEWS In SQL :-

CREATE VIEW view1 AS
SELECT customer_id, name FROM customers;

SELECT * FROM view1;

CREATE VIEW view2 AS
SELECT c.customer_id, c.name, o.order_id
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

SELECT * FROM view2;

DROP VIEW view2;

-- Index in SQL  :- data retrival faster.

CREATE TABLE Account (
account_id INT PRIMARY KEY,
name VARCHAR(50),
balance DECIMAL(10, 2),
branch VARCHAR(50)
);

INSERT INTO Account
VALUES
(1, 'Adam', 500.00, 'Mumbai'),
(2, 'Bob', 300.00, 'Delhi'),
(3, 'Charlie', 700.00, 'Bangalore'),
(4, 'David', 1000.00, 'Noida');


SELECT * FROM account;

-- Single column index 

CREATE INDEX idx_branch ON account(branch);

SHOW INDEX FROM account;

SELECT *
FROM account
WHERE branch = 'Mumbai';

-- multiple column use in index

CREATE INDEX idx2 ON account(branch, balance);
 
SHOW INDEX FROM account;

DROP INDEX idx2 ON account;

-- STORE PROCEDURES :-

DELIMITER $$

CREATE PROCEDURE check_balance(IN acc_id INT, OUT bal DECIMAL(10, 2))
BEGIN
     SELECT balance INTO bal
     FROM account
     WHERE account_id = acc_id;
END $$
    
DELIMITER ;

CALL check_balance(1, @balance);
SELECT @balance;


DROP PROCEDURE IF EXISTS check_balance;