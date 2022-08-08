logged_user = False
# if logged_user:
#     msg = 'Usuário Logado.'
# else:
#     msg = 'Usuário precisa Logar.'
msg = 'Usuário Logado' if logged_user else 'Usuário precisa logar.'
print(msg)
idade = input('Qual sua idade? ')
if not idade.isnumeric():
    print('Digite apenas números')
else:
    idade = int(idade)
    ismaior = (idade >= 18)
    msg = 'pode acessar' if ismaior else 'Não pode acessar.'
    print(msg)
