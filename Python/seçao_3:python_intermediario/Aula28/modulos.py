from sys import platform as so
from random import randint

print('sys:')
print(so)
print('random: ')
for i in range(10):
    print(randint(0, 10))
