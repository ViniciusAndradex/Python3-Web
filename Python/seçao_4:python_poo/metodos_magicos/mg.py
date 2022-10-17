class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste

    def __init__(self):
        print('Eu sou init')

    def __call__(self, *args, **kwargs):
        result = 1
        for i in args:
            result *= i
        print(result)

    def __setattr__(self, key, value):
        print(f'Detectei a chave {key} com valor {value}')
        self.__dict__[key] = value

    def __del__(self):
        print('Coleteiiiii')

    def __str__(self):
        return "<Clas Identifie>"

    def __len__(self):
        return 55


a = A()
b = A()
a.nome = 'Jota'

print(a == b)
print(a)
a(15, 20, jota='Jota')


