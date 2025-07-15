#! python


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55....
def fibonacci():
    penultimo = 0
    ultimo = 1
    # end=',' para seguir na mesma linha
    print(f'{penultimo}, {ultimo}', end=',')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')  # end=',' para seguir na mesma linha
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()
