
try:
    open('tarefas.txt', 'x')
except Exception:
    print('O arquivo já foi criado!')

while True:
    menu = int(input('''
    [1] Adicionar Tarefa
    [2] Listar Tarefas
    [3] Desfazer tarefa
    [4] Refazer tarefa
    [0] Sair
    - Opção: '''))
    with open('tarefas.txt', 'a+') as file:
        file.
        if menu == 1:
            tarefa = input('Adicione Tarefa: ')
            file.write(tarefa)
        elif menu == 2:
            print(file.read(), end='')
        elif:
        break
