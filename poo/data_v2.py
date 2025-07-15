# CONSTRUTOR
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):  # toda função/metodo dentro de uma class é obrigatorio começar com self
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 4, 2012)
# d1.dia = 3
# d1.mes = 6
# d1.ano = 1996
print(d1)

d2 = Data(1, 1, 1991)
# d2.dia = 18
# d2.mes = 2
# d2.ano = 1995
print(d2)
