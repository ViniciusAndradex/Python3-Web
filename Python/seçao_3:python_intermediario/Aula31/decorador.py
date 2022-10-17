from time import time, sleep


def master(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        result = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A funcao {funcao.__name__} levou {tempo:.2f} ms')
    return interna


@master
def demora():
    for i in range(10000):
        print(i)


demora()
