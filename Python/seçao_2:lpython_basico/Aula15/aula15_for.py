texto = 'Python'

for i in texto:
    if i == 't':
        # continue
        # break
        print(f'{i.upper()} - ', end='')
    else:
        print(f'{i} - ', end='')

print('-' * 10)
for c in range(10):
    print(c)
