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
            item = input('1 - SELECT\n2 - INSERT\n3 - DELETE\n4 - UPDATE\n5- SAIR\nOpcao n°: ').strip
            if not(int(item)):
                raise ValueError('Digite um número')
        except ValueError as error:
            print(error)
        else:
            break
    
    if item == 1:
        pass
    if item == 2:
        while True:
            try:
                tabela_insert = input('Digite a tabela [roles, profile, users]: ').strip().lower()
                if tabela_insert not in 'rolesprofileusers':
                    raise TabelaError('Digite uma tabela Existente')
            except TabelaError as tabela_error:
                print(tabela_error)
            else:
                break
        while True:
            try:
                item = input('Numero de inserções: ').strip
                if not(int(item)):
                    raise ValueError('Digite um número')
            except ValueError as value_error:
                print(value_error)
            else:
                break
        
        dados =list()
        
        while True:
            first_name = input('Digite seu nome: ').strip()
            last_name = input('Digite seu nome: ').strip()
            email = input('Digite seu nome: ').strip()
            password = input('Digite seu nome: ').strip()
            salary = float(input('Digite seu nome: '))

            compilacao_dados = (first_name, last_name, email, password, salary)
            dados.append(compilacao_dados)
        
        

    if item == 3:
        pass
    if item == 4:
        pass
    if item == 5:
        print('OBRIGADO utilizar meu banco de dados.')
        break