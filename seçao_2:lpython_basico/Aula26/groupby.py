from itertools import groupby

alunos = [
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Jorge', 'nota': 'B'},
    {'nome': 'Mario', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'D'},
    {'nome': 'Gustavo', 'nota': 'B'},
    {'nome': 'Patrick', 'nota': 'C'},
    {'nome': 'João', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'D'},
    {'nome': 'Manuel', 'nota': 'A'},
]

ordenar = (lambda item: item['nota'])
alunos.sort(key=ordenar)
alunos_agrupados = groupby(alunos, ordenar)

for agrupamento, agrupado in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for valores in agrupado:
        print(valores)
    print()
