# Validando existência do argumento
#! python

# primeira forma de exibir o indice 0
from math import pi  # importando o pi do MATH
# importei a Função (Sys) para poder digitar na linha de comando do TERMINAL
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("É necessario informar o raio do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO + 'O raio deve ser um valor numérico!' +
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do Círculo É:', area)
    print(dir())
