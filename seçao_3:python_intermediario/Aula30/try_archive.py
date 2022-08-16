# try:
#     file = open('abc.txt', 'w+')
#     file.write('João\n')
#     file.seek(0)
#     print(file.read(), end='')
# finally:
#     file.close()

with open('abc.txt', 'a+') as file:
    file.write('OMG')
    file.seek(0)
    print(file.read())
