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

while True:
    print(f'{"-"* 5} MENU {"-" * 5}')
    while True:
        try:
            item = input('1 - SELECT\n2 - INSERT\n3 - DELETE\n4 - UPDATE\n5- SAIR\nOpcao n°: ')
            if isinstance(item, int):
                raise ValueError('Digite um número')
            else:
                item = int(item)
        except ValueError as error:
            print(error)
        else:  
            if 0 < item <= 5:
                break
    
    if item == 1:
        pass
    if item == 2:
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
        
        dados = list()
        contador = 0
        while contador < num_inserts:
            first_name = input('Digite seu primeiro nome: ')
            last_name = input('Digite seu ultimo nome: ')
            email = input('Digite seu email: ')
            password = input('Digite uma senha: ')
            salary = float(input('Digite seu salario: '))
            print('-' * 20)

            compilacao_dados = (first_name, last_name, email, password, salary)
            dados.append(compilacao_dados)
            contador += 1


        crud.insert(tabela_insert, dados)
    if item == 3:
        pass
    if item == 4:
        pass
    if item == 5:
        print('OBRIGADO utilizar meu banco de dados.')
        break