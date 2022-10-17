nome = 'VInicius ANdrade'
iterador = iter(nome)
gerador = (letra for letra in nome)
# try:
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
# except:
#     pass
print('EAI?')
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print('for do gerador')
for c in gerador:
    print(c)
print('Outro for')
for c in gerador:
    print(c)
