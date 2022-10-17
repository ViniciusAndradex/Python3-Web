# def fala_oi():
#     print('oi')
#
# variavel = fala_oi
#
# variavel()
# print(type(variavel))

# Função decoradora
def master(funcao):
    def slave(*args, **kwargs):
        print('Decorei')
        funcao(*args, **kwargs)
    return slave


# decorada
@master
def fala_oi():
    print('oi')


fala_oi()