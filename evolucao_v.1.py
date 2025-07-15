#! python

class Humano:
    # atributo de classe
    # esse atributo de Classe é compartilhado por todas as instãncias
    especie = "Homo sapiens"

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        # mesmo self.especie tendo o mesmo nome do atributo da Classe, ele prevalece.
        self.especie = "Homo Neanderthalensis"
        return self  # chamando o mesmo objeto/instancia


if __name__ == '__main__':
    jose = Humano('Jose')
    abrao = Humano('Abrao').das_cavernas()

print(f'Homo.especie: {Humano.especie}')
print(f'Homo.especie: {jose.especie}')
print(f'Homo.especie: {abrao.especie}')
