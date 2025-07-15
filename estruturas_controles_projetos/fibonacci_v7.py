#! python


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55....
def fibonacci(quantidade):
    resultado = [0, 1]
    for i in range(2, quantidade):  # utilizando o for  e o range
        resultado.append(sum(resultado[-2:]))  # adicionando função soma sum()
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequência
    for fib in fibonacci(20):
        print(fib)
