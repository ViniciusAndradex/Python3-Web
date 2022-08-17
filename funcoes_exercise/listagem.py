def lines():
    print('-' * 40)


def cabecalho():
    print('\033[1;34mLISTA DE TAREFAS: \033[m')


def listar(tarefa):
    print(f'\t- {tarefa}', end='')


def menu():
    print('''
        [1] Adicionar Tarefa
        [2] Listar Tarefas
        [3] Desfazer tarefa
        [4] Recuperar tarefa
        [0] Sair
        - Opção: ''', end='')
