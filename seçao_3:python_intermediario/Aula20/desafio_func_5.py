def master(func):
    return func()


def func2(*args):
    args = (1, 8, 3, 5)
    return args


var = master(func2)
print(var)
print(*var)
