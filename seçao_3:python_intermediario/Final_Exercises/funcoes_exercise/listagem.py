def lines():
    print('-' * 40)


def cabecalho():
    print('\033[1;34mLISTA DE TAREFAS: \033[m')


def listar(tarefa):
    print(f'\t- {tarefa}', end='')
