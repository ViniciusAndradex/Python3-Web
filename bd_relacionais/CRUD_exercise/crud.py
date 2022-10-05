import pymysql.cursors
from contextlib import contextmanager

class CRUD():

    @contextmanager
    def conectar(self):
        conexao = pymysql.connect(host='localhost',
                            user='usuario',
                            password='senha',
                            database='base_de_dados',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        try:
            yield conexao
        finally:
            conexao.close()


    def insert_users(self, lista):
        with self.conectar() as conectar:
            with conectar.cursor() as cursor:
                sql = 'INSERT INTO users (first_name, last_name, email, password_hash, salary) VALUES (%s, %s, %s, %s, %s)'

                cursor.executemany(sql, lista)

                conectar.commit()
    def insert_profiles(self, lista):
        with self.conectar() as conectar:
            with conectar.cursor() as cursor:
                sql = 'INSERT INTO profiles (bio, description, user_id) SELECT CONCAT("Bio de ", first_name), CONCAT("Description de ", first_name), id FROM users WHERE email IN (%s) ORDER BY created_at DESC ' 

                cursor.executemany(sql, lista)

                conectar.commit()

    def insert_users_roles(self, lista):
        with self.conectar() as conectar:
            with conectar.cursor() as cursor:
                sql = 'INSERT IGNORE INTO users_roles (user_id, role_id) SELECT id, (SELECT id FROM roles WHERE id = %s) FROM users WHERE email IN (%s)'

                cursor.executemany(sql, lista)

                conectar.commit()
        



    