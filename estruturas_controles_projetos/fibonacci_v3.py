#! python


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55....
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    # end=',' para seguir na mesma linha
    print(f'{penultimo},{ultimo}', end=',')
    while ultimo < limite:
        penultimo,  ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=',')  # end=',' para seguir na mesma linha


if __name__ == '__main__':
    fibonacci(20000)
