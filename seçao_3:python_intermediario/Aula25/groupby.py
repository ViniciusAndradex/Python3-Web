from itertools import groupby, tee
alunos = [
    {'nome': 'Anderson', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'D'},
    {'nome': 'Henrique', 'nota': 'D'},
    {'nome': 'Jorge', 'nota': 'A'},
    {'nome': 'Wilker', 'nota': 'B'},
    {'nome': 'Icaro', 'nota': 'C'},
    {'nome': 'Adriele', 'nota': 'C'},
    {'nome': 'nadyla', 'nota': 'B'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Francisco', 'nota': 'D'},
    {'nome': 'Ana', 'nota': 'C'},
    {'nome': 'Manoel', 'nota': 'A'},
]

ordenar = (lambda item: item['nota'])
alunos.sort(key=ordenar)
alunos_agrupados = groupby(alunos, ordenar)

for notas, agrupados in alunos_agrupados:
    va1, va2 = tee(agrupados)
    print(f'Agrupamento: {notas}')
    for agrupamento in va1:
        print('\t', agrupamento)
    qtd = len(list(va2))
    print(f'\t{qtd} alunos que tiraram a nota {notas}')
    print()
