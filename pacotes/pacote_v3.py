# Módulos com o mesmo nome
from pacote1 import modulo1
from pacote2 import modulo1 as modulo_sub


print('soma', modulo1.soma(3, 2))
print('subtracao', modulo_sub.subtracao(3, 2))