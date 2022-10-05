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

import functions

while True:
    print(f'{"-"* 8} MENU {"-" * 8}')
    while True:
        try:
            item = input('1 - SELECT\n2 - INSERT\n3 - DELETE\n4 - UPDATE\n5 - SAIR\nOpcao n°: ')
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
        functions.config_tabela()
    if item == 3:
        pass
    if item == 4:
        pass
    if item == 5:
        print('OBRIGADO utilizar meu banco de dados.')
        break