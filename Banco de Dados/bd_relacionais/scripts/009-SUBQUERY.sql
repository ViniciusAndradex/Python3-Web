INSERT INTO users_roles (user_id, role_id) SELECT id, (SELECT id FROM roles  WHERE id > 1 ORDER BY RAND() LIMIT 1) 
as perm from users;

-- O ignore evita que o código quebre;
INSERT IGNORE INTO users_roles (user_id, role_id) SELECT id, (SELECT id FROM roles  WHERE id > 1 ORDER BY RAND() LIMIT 1) 
as perm from users ORDER BY RAND() LIMIT 5;