#! python


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55....
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    # end=',' para seguir na mesma linha
    print(f'{penultimo},{ultimo}', end=',')
    while ultimo < limite:
        proximo = penultimo + ultimo
        print(proximo, end=',')  # end=',' para seguir na mesma linha
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci(20000)
