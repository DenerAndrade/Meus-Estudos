# if True:
#     print('Vai demorar muitoooooooo')


# de random importe a função randint
# a função randint retorna um número ALEÁTORIO entre o número inicial e o número final
from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

# enquanto numero_informado for diferente do numero_secreto execute
while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o numero: '))

print('Numero secreto {} foi encontrado!'.format(numero_secreto))
