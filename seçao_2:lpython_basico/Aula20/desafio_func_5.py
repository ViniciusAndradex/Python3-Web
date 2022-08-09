def func1(func):
    return func


def func2(*args):
    return args


var = func1(func2(1, 2, 3, 4, 5))
print(var)
print(*var)
