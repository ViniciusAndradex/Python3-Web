def lista_cliente(clientes_itereavel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_itereavel)
    return lista


cliente1 = lista_cliente(['João', 'marcos'])
cliente2 = lista_cliente(['<a>'])

print(cliente2)
print(cliente1)
