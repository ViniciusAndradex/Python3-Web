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
    
    def insert(self, tabela, *args):
        with self.conectar() as conecta:
            with conecta.cursor() as cursor:
                sql = (f'INSERT INTO {tabela} (first_name, last_name, email, password_hash, salary) VALUES (?, ?, ?, ?, ?)')
                cursor.execute(sql, args)

                conecta.commit()


    