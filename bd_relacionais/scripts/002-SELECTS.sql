SELECT * FROM users u;
SELECT email, u.id FROM users u ;
SELECT  * FROM users u WHERE created_at BETWEEN "2020-08-22 13:41:06" AND "2021-04-16 22:20:05" AND 
u.id BETWEEN 110 AND 128;
SELECT * FROM  users u WHERE id IN (110, 115, 120, 125) AND first_name  IN ("Lucian", 'Brittany');
SELECT * FROM users u WHERE first_name LIKE 'na%a';
SELECT id, first_name, email FROM users u WHERE id BETWEEN 100 AND 150 ORDER BY created_at ASC,
first_name DESC;
SELECT id, first_name, email FROM users u WHERE id BETWEEN 110 AND 150 ORDER BY id ASC LIMIT 2 OFFSET 2;