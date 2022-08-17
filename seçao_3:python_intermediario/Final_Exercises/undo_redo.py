from funcoes_exercise.listagem import lines, menu
from funcoes_exercise.undo_redo_func import adicionar, apresentar, remover, devolver

try:
    open('tarefas.txt', 'x')
except Exception:
    print('O arquivo já foi criado!')

buffer = ''

while True:
    while True:
        try:
            menu()
            opc = input()
            opc = int(opc)
            if 0 > opc or opc > 4:
                raise ValueError('Escolha um valor entre [0 | 4]')
        except ValueError as error:
            print(f'Por favor digite um número [{error}]\n')
        else:
            break
    lines()
    with open('tarefas.txt', 'a+') as file:
        if opc == 1:
            adicionar(file)
            lines()
        elif opc == 2:
            apresentar(file)
            lines()
        elif opc == 3:
            file.seek(0)
            var = file.readlines()
            if var:
                buffer = remover(var, buffer=buffer)
                print(f'Tarefa Removida: {buffer}', end='')
            else:
                print('Você não possui nenhuma tarefa')
            lines()
        elif opc == 4:
            file.seek(0)
            var = file.readlines()
            if buffer:
                buffer = devolver(var, buffer)
                print(f'Tarefa Recuperada: {buffer}', end='')
            else:
                print('Você não possui nenhuma tarefa')
            lines()
        elif opc == 0:
            break
