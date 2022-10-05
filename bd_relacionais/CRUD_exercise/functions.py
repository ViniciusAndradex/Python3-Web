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
            tabela_insert = input('Digite a tabela [users_roles, profiles, users]: ').lower()
            if tabela_insert != 'users_roles' and tabela_insert != 'profiles' and tabela_insert != 'users':
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
    if tabela_insert == 'users':
        tabela_users(num_inserts)
    elif tabela_insert == 'profiles':
        tabela_profiles(num_inserts)
    else:
        tabela_users_roles(num_inserts)


def tabela_users(num_insert):
    dados = list()

    for c in range(num_insert):
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

    crud.insert_users(dados)

    print('Inserção feita com sucesso!\n\n')


def tabela_profiles(num_insert):
    dados = list()

    for c in range(num_insert):
        while True:
            email = input('Digite o e-mail para a criação do perfil: ')
            if email == '':
                print('Digite um email!')
            else: 
                break
        dados.append(email)
        print('Perfil criado com sucesso!')
    
    crud.insert_profiles(dados)

    print('Os perfis solicitados foram cadastrados!\n\n')


def tabela_users_roles(num_insert):
    dados = list()

    for c in range(num_insert):
        while True:
            email = input('Digite o e-mail para adicição de uma função: ')
            if email == '':
                print('Digite um email!')
            else: 
                break
        while True:
            try:
                func = input("""
    2 - POST
    3 - PUT
    4 - DELETE
    5 - GET
    - OPCAO: """)
                if isinstance(func, int):
                    raise ValueError('Digite um número')
            except ValueError as value_error:
                print(value_error)
            else:
                func = int(func)
                break

        dados.append(func, email)
        print('Função armazenada com SUCESSO!')
    
    crud.insert_users_roles(dados)

    print('Função adicionada com SUCESSO!')
    