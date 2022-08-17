from funcoes_exercise.listagem import cabecalho, listar


def adicionar(archive):
    tarefa = input('Adicione Tarefa: ')
    tarefa = tarefa + '\n'
    archive.write(tarefa)


def apresentar(archive):
    archive.seek(0)
    cabecalho()
    for item in archive.readlines():
        listar(item)


def remover(var, buffer):
    buffer = var[-1]
    var.remove(var[-1])
    with open('tarefas.txt', 'w+') as file:
        for item in var:
            file.write(item)
    return buffer


def devolver(var, buffer):
    var.append(buffer)
    with open('tarefas.txt', 'w+') as file:
        for item in var:
            file.write(item)
    return buffer
