MAIOR_IDADE = 18 # Contante 


class Pessoa: #classe pai
    def __init__(self, nome, idade): # construtor
        self.nome = nome # inicializar
        self.idade = idade # inicializar

    def __str__(self): # função que converte objeto pra string
        if not self.idade:
            return self.nome
        return f'{self.nome} ({self.idade} anos)'

    def is_adulto(self):
        return (self.idade or 0) > MAIOR_IDADE
