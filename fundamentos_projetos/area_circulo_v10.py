# OBETENDO ARGUMENTO VIA TERMINAL /PASSANDO VALOR DO RAIO NO PRÓPIO TERMINAL
#! python
from math import pi  # importando o pi do MATH
# importei a Função (Sys) para poder digitar na linha de comando do TERMINAL
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    # print(sys.argv[2]) teste para ver o que estava exibindo na linha de comando do terminal
    # Deferente do input, o Raio recebe o valor digitado na linha do terminal
    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do Círculo É:', area)
