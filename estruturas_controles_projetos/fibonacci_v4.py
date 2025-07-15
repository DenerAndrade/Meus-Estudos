#! python


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55....
def fibonacci(limite):
    resultado = [0, 1]  # lista
    while resultado[-1] < limite:
        # acessando o indice da lista negativo/ ao contrario[-2] + [-1]
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(100):
        print(fib)
