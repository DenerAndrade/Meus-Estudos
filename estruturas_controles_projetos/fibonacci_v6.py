

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55....
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))  # adicionando função soma sum()
        if len(resultado) == quantidade:  # len é o tamanho do resultado for \
            # igual á quantidade
            break  # pare/ interrompa
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequência
    for fib in fibonacci(15):
        print(fib)
