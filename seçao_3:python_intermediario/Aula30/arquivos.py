file = open('abc.txt', 'w+')
file.write('Love\n')
file.write('and\n')
file.write('Furious\n')
file.seek(0, 0)
print(file.read())
print('-' * 10)

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

print('-' * 10)
file.seek(0, 0)
print(file.readlines())

for c in file.readlines():  # Or file.
    print(c, end='')
file.close()
