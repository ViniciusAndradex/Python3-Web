d1 = {'chave1': 'valor da chave', 'a': 'valor'}
# d1 = dict(chave1='valor da chave')
d1[(15,)] = 'valor da nova chave'
d1[(15,)] = 'valor da nova chave_mudei'
d1.update({(15,): 'valor da nova chave_mudei_denovo'})
print(d1)
print('chave1' in d1)
print('chave1' in d1.values())
if (15,) in d1:
    print(d1[(15,)])
print(d1.get('chave1'))
print('KEYS')
for k in d1:
    print(k, end=' ')
print()
print('VALUES')
for v in d1.values():
    print(v, end=' ')
print()
print('KEYS AND VALUES')
for v in d1.items():
    print(v[0], '-', v[1], '|', end=' ')
    # or print(k, v, end=' ')
print()
del d1['chave1']

