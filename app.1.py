# HERANÇA

class Pessoa:
    def __init__(self, nome, cpf, altura):
        self.cpf = cpf
        self.altura = altura
        self.nome = nome


class Secretaria(Pessoa):
    def __init__(self, id_secretaria, nome, cpf, altura):
        super().__init__(nome, cpf, altura)  # super é uma referência a classe Pessoa
        self.id_secretaria = id_secretaria


class Vendedor(Pessoa):
    def __init__(self, total_vendas, nome, cpf, altura):
        super().__init__(nome, cpf, altura)  # super é uma referência a classe Pessoa
        self.total_vendas = total_vendas


s1 = Secretaria('18', 'Joao', '44444', '177')
v1 = Vendedor('05', 'Beto', '55555', '189')
