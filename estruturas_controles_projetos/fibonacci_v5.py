

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55....
def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))  # adicionando função soma sum()
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(100):
        print(fib)
