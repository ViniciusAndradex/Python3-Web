class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:
            del namespace['attr_classe']  # Não permite a criação de outro atributo de mesmo nome e nem uma sobreposição
        # if 'b_fala' not in namespace:
        #     print(f'Crie o método b_fala em {name}')
        # else:
        #     if not callable(namespace['b_fala']):
        #         print('O método b_fala precisa ser método!')
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'


C = type('C', (A,), {'attr': 'Olá mundo!'})


class B(A):
    attr_classe = 'Valor B'


b = B()
print(b.attr_classe)
print(C.attr)
