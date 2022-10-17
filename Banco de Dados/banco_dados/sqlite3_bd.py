import sqlite3

conexao = sqlite3.connect('basesdedados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                 'nome TEXT,'
#                 'peso REAL'
                # ')')
# Desta forma se é enviado uma tupla
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
# Desta um dicionário.
# cursor.execute(
    # 'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Mario', 'peso': 80})
# Desta estamos enviando também o ID
# cursor.execute(
    # 'INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Pedro', 'peso': 89})
# cursor.execute('DELETE FROM clientes WHERE clientes.id > 0')
# conexao.commit()

# cursor.execute('UPDATE clientes SET nome = :nome WHERE id =:id', 
#                 {'nome': 'Joana', 'id': 8})
# cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 7})

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 85})

# cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    # print(linha)
    nome, peso = linha

    print(nome, peso)

cursor.close()
conexao.close()