s1 = {1, 2, 3, 4, 5}
s1.add(8)
s1.add(9)
s1.discard(9)
s1.update('Python')
print(s1, type(s1))
for v in s1:
    print(v)
print('-' * 10)
lista = [1, 1, 2, 4, 3, 5, 'Lula', 'Lula']
lista = set(lista)
# Nessa posição eu estou fazendo um casting para eliminar os meus elementos duplicados, a única coisa
# que temos que ter cuidado é que ordem foi completamente bagunçada.
lista = list(lista)

print(lista)
print('-' * 10)
s = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3, 4, 10, 11}
s3 = s | s2
s4 = s & s2
s5 = s - s2
s6 = s ^ s2
print(s3)
print(s4)
print(s5)
print(s6)
print('-' * 10)
l1 = ['joao', 'maria', 'jorge']
l2 = ['joao', 'maria', 'jorge', 'jorge', 'maria']

if set(l1) == set(l2):
    print(l1, l2)
else:
    print('São diferentes!')
