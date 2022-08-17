from funcoes_exercise.listagem import listar, cabecalho, lines
from funcoes_exercise.undo_redo_func import remove

try:
    open('tarefas.txt', 'x')
except Exception:
    print('O arquivo já foi criado!')

while True:
    while True:
        try:
            menu = input('''
    [1] Adicionar Tarefa
    [2] Listar Tarefas
    [3] Desfazer tarefa
    [4] Refazer tarefa
    [0] Sair
    - Opção: ''')
            menu = int(menu)
        except ValueError:
            print('Por favor digite um número [0 - 4]\n')
        else:
            break
    lines()
    with open('tarefas.txt', 'a+') as file:
        if menu == 1:
            tarefa = input('Adicione Tarefa: ')
            tarefa = tarefa + '\n'
            file.write(tarefa)
            lines()
        elif menu == 2:
            file.seek(0)
            cabecalho()
            for item in file.readlines():
                listar(item)
            lines()
        elif menu == 3:
            for line in file.readlines():
                file.

        elif menu == 4:
            pass
        elif menu == 0:
            break
