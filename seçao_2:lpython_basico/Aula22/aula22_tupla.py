t1 = (1, 2, 3, 'a', 'Vinicius') * 3
t2 = 6, 7, 8
t3 = t1 + t2
a, b, c, *_ = t3

print(t1[2])
print(*t1)
print(t1[2:])
print(a, b, c, _)
