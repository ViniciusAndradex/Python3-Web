try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../../'
            )
        )
    )
except ImportError:
    raise
from bd_relacionais.CRUD_exercise.crud import CRUD
from bd_relacionais.CRUD_exercise.exceptions_crud import TabelaError

crud = CRUD()

def config_tabela():
    while True:
        try:
            tabela_insert = input('Digite a tabela [roles, profiles, users]: ').lower()
            if tabela_insert != 'roles' and tabela_insert != 'profiles' and tabela_insert != 'users':
                raise TabelaError('Digite uma tabela Existente')
        except TabelaError as tabela_error:
            print(tabela_error)
        else:
            break
    while True:
        try:
            num_inserts = input('Numero de inserções: ')
            if isinstance(num_inserts, int):
                raise ValueError('Digite um número')
        except ValueError as value_error:
            print(value_error)
        else:
            num_inserts = int(num_inserts)
            break
    tabela_users(tabela_insert, num_inserts)


def tabela_users(tabela, num_insert):
    dados = list()
    contador = 0
    while contador < num_insert:
        while True:
            first_name = input('Digite seu primeiro nome: ')
            if first_name == '':
                print('Campo Obrigatório!')
            else:
                break
        last_name = input('Digite seu ultimo nome: ')
        while True:
            email = input('Digite seu email: ')
            if email == '':
                print('Campo Obrigatório!')
            else:
                break
        while True:
            password = input('Digite uma senha: ')
            if password == '':
                print('Campo Obrigatório!')
            else:
                break
        salary = float(input('Digite seu salario: '))
        print('-' * 20)

        compilacao_dados = (first_name, last_name, email, password, salary)
        dados.append(compilacao_dados)
        contador += 1


    crud.insert(tabela, dados)

    print('Inserção feita com sucesso!\n\n')


def tabela_profiles(tabela, num_insert):
    pass