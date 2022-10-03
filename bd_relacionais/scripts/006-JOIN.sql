SELECT u.id  as uid, p.id as pid, p.bio, u.first_name FROM users as u INNER JOIN profiles p ON u.id = p.user_id
WHERE u.first_name LIKE 'v%' ORDER BY u.id  DESC LIMIT 3;

SELECT u.id  as uid, p.id as pid, p.bio, u.first_name FROM users as u LEFT JOIN profiles p ON u.id = p.user_id;

SELECT u.id  as uid, p.id as pid, p.bio, u.first_name FROM users as u RIGHT JOIN profiles p ON u.id = p.user_id;
