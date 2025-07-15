#! python
class potencia:
    # Calcula uma pontencia especifica
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


class ttols:
    # Calcula uma pontencia especifica
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = potencia(2)
    cubo = ttols(4)

    if callable(quadrado) and callable(cubo):
        print(f'3² => {quadrado(3)}')
        print(f'2² => {cubo(3)}')
        print(f'5² => {cubo(5)}')
        print(potencia(4)(2))
