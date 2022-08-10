def func1(func):
    return func()


def func2(*args):
    args = (1, 8, 3, 5)
    return args


var = func1(func2)
print(var)
print(*var)
