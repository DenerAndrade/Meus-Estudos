def executar(funcao):
    funcao()


def bom_dia():
    print('Bom dia')


def boa_tarde():
    print('Boa tarde')


def boa_noite():
    print('Boa noite')


if __name__ == '__main__':
    executar(bom_dia)  # executando uma função a partir de outra função
    executar(boa_tarde)  # executando uma função a partir de outra função
    executar(boa_noite)  # executando uma função a partir de outra função
