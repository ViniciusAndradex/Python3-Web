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


    def insert(self, tabela, lista):

        if tabela == 'users':
            with self.conectar() as conectar:
                with conectar.cursor() as cursor:
                    sql = 'INSERT INTO users (first_name, last_name, email, password_hash, salary) VALUES (%s, %s, %s, %s, %s)'

                    cursor.executemany(sql, lista)

                    conectar.commit()

        if tabela == 'profiles':
            with self.conectar() as conectar:
                with conectar.cursor() as cursor:
                    sql = 'INSERT INTO profiles (bio, description, user_id) SELECT CONCAT("Bio de ", first_name), CONCAT("Description de ", first_name), id FROM users WHERE created_at >  "2022-10-05 13:2:00"' 

                    cursor.executemany(sql, lista)

                    conectar.commit()
            



    