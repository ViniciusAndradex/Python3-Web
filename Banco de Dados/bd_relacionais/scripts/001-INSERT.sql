use base_de_dados;
show tables;
describe users ;

INSERT INTO users (first_name, last_name, email,password_hash) values 
("jorge","","jorge@gmail.com", "d_hash"), 
("Nice","Andrade","nice@gmail.com","e_hash");

INSERT INTO profiles (bio, description, user_id) 
SELECT CONCAT('Bio de ', first_name), CONCAT('Description de ', first_name), id FROM users;
DELETE FROM profiles;