

from math import pi  # importando o pi do MATH


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informa o raio: ')
    area = circulo(raio)
    print('Area do Circulo:', area)
