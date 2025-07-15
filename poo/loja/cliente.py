# IMPORTE RELATIVO
from .pessoa import Pessoa


def get_data(compra):
    return compra.data

# classe (Cliente) herda da Superclasse (Pessoa)
class Cliente(Pessoa):
    def __init__(self, nome, idade): # contrutor
        super().__init__(nome, idade) # chama o construtor da classe Pai
        self.compras = [] # inicializar

    def registrar_compra(self, compra):
        self.compras.append(compra) # adiciona (compra) dentro da lista de self.compras

    def get_data_ultima_compra(self):
        return None if not self.compras else \
            sorted(self.compras, key=get_data)[-1].data # ordena a lista a partir da data da compra

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total
