import pymysql.cursors
from contextlib import contextmanager

# CRUD - COMPLETE

@contextmanager
def conecta():
    conexao = pymysql.connect(host='10.50.21.37',
                            user='suporte',
                            password='v.andrade',
                            database='clientes',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
        yield conexao
    finally:
        conexao.close()


# Insere 1 DADO
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) Values (%s, %s, %s, %s)'
#         cursor.execute(sql, ('Wilker', 'Alberto', 22, 48))

#         conexao.commit()
# Insere vários dados
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) Values (%s, %s, %s, %s)'
        
#         dados = [
#             ('Mauricio', 'Fagundes', 85, 45),
#             ('Jobs', 'Hernan', 45, 47),
#             ('Blockaniston', 'Job', 28, 89)
#         ]

#         # Permite que seja enviado variaos dados ao mesmo tempo envitando execuções repetidas.
#         cursor.executemany(sql, dados)

#         conexao.commit()
# Deleta 1 dado
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         delete = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(delete, (6,))

#         conexao.commit ()
# Exclui vários
# with conecta() as conexao:
    # with conexao.cursor() as cursor:
        # deletemany = 'DELETE FROM clientes WHERE id = %s'
        # OR
        # deletemany = 'DELETE FROM clientes WHERE id IN (%s...)'
        # Exclua entre x e y 
        # sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
        # cursor.execute(sql, (10, 13))        
        # dados = [
        #     (2,),
        #     (4,),
        #     (8,)
        # ]

        # cursor.executemany(deletemany, dados)
        # conexao.commit()

# with conecta() as conexao:
#     with  conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s, idade=%s WHERE id = %s'
#         cursor.execute(sql, ('Manel', 26, 3))

#         conexao.commit()
        
with conecta() as conexao:
    # O with garante o fechamento do meu cursor;
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 50')
        resultado = cursor.fetchall()

        for valores in resultado:
            print(valores)
