
def fibonacci(sequencia=[0, 1]):
    # Uso de mutáveis com o valor default (armadilha)
    # somando as posições da lista
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
