# IMPORTE RELATIVO
from .pessoa import Pessoa


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):  # Construtor
        super().__init__(nome, idade)  # Chama a super classe
        self.salario = salario  # inicializar
