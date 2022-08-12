def divisao(n, n1):
    try:
        return n / n1
    except ZeroDivisionError as erro:
        print('Log: ', erro)
        raise ZeroDivisionError("O Valor não pode de forma alguma ser zero.")


def divisao1(n, n1):
    if n1 == 0:
        raise ValueError(f"O n1={n1} não pode ser Zero(0).")
    return n / n1


try:
    print(f'{divisao(2, 0)}')
except ZeroDivisionError as error:
    print(error)
