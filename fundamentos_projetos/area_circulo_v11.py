# Validando existência do argumento

# primeira forma de exibir o indice 0
from math import pi  # importando o pi do MATH
# importei a Função (Sys) para poder digitar na linha de comando do TERMINAL
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("É necessario informar o raio do circulo.")
        # primeira forma de exibir o indice [0] da linha de comando do terminal
        print("Sintaxe: {} <raio>".format(sys.argv[0]))
        # primeira forma de exibir o indice [0] da linha de comando do terminal
        print('Sintaxe:', sys.argv[0], '<raio>')
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do Círculo É:', area)
