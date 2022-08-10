perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'resposta': {
            'a': '1',
            'b': '4',
            'c': '3',
            'd': '8'
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2?',
        'resposta': {
            'a': '4',
            'b': '10',
            'c': '6',
            'd': '8'
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1+2?',
        'resposta': {
            'a': '4',
            'b': '2',
            'c': '6',
            'd': '3'
        },
        'resposta_certa': 'd',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1-1?',
        'resposta': {
            'a': '4',
            'b': '2',
            'c': '1',
            'd': '0'
        },
        'resposta_certa': 'd',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8/4?',
        'resposta': {
            'a': '4',
            'b': '2',
            'c': '1',
            'd': '0'
        },
        'resposta_certa': 'b',
    },

}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha entre as opções abaixo:')
    for rk, rv in pv['resposta'].items():
        print(f'\t{rk}) {rv}')
    resp_user = input('Sua resposta: ')
    if resp_user == pv['resposta_certa']:
        print('Acertou!')
        respostas_certas += 1
    else:
        print('ERROU!')
    print()
qtd_perguntas = len(perguntas)
porcentagem = respostas_certas / qtd_perguntas * 100
print(f'Tivemos {qtd_perguntas} perguntas e você acertou {porcentagem}%.')
