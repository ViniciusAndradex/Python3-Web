SELECT first_name, COUNT(id) as total  FROM users GROUP BY first_name ORDER BY total DESC ;

SELECT u.first_name, COUNT(u.id) as total FROM users as u LEFT JOIN profiles as p ON p.user_id = u.id 
WHERE u.first_name  = 'Xyla' GROUP BY u.first_name ORDER BY total DESC LIMIT 5; 

SELECT MAX(salary) as max_salary, 
MIN(salary) as min_salary, 
AVG(salary) as media_salary, 
SUM(salary) as sum_salary,
COUNT(salary) as num_salary
FROM users WHERE first_name = 'carly';

SELECT
u.first_name,
MAX(u.salary) as max_salary, 
MIN(u.salary) as min_salary, 
AVG(u.salary) as media_salary, 
SUM(u.salary) as sum_salary,
COUNT(u.id) as total
FROM users as u LEFT JOIN profiles as p ON p.user_id = u.id WHERE u.id > 70
GROUP BY first_name ORDER BY total DESC LIMIT 3; 
