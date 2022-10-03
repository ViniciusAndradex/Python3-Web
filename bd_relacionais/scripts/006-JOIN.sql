SELECT u.id  as uid, p.id as pid, p.bio, u.first_name FROM users as u INNER JOIN profiles p ON u.id = p.user_id
WHERE u.first_name LIKE 'v%' ORDER BY u.id  DESC LIMIT 3;

SELECT u.id  as uid, p.id as pid, p.bio, u.first_name FROM users as u LEFT JOIN profiles p ON u.id = p.user_id;

SELECT u.id  as uid, p.id as pid, p.bio, u.first_name FROM users as u RIGHT JOIN profiles p ON u.id = p.user_id;

-- JOIN
SELECT u.id as uid, u.first_name, p.bio, r.name  FROM users as u LEFT JOIN profiles as p ON u.id = p.user_id
INNER JOIN users_roles as ur ON u.id = ur.user_id INNER JOIN roles as r ON ur.role_id = r.id ORDER BY uid ASC;

UPDATE users as u 
INNER JOIN profiles as p ON p.user_id = u.id SET p.bio = CONCAT(p.bio, ' ATUALIZADO')  WHERE u.first_name = 'Thaddeus'; 

DELETE p FROM  users as u 
INNER JOIN profiles as p ON p.user_id = u.id WHERE u.first_name = 'xyla'; 

SELECT u.first_name, p.bio  FROM users as u 
LEFT JOIN profiles as p ON p.user_id = u.id WHERE u.first_name = 'xyla'; 