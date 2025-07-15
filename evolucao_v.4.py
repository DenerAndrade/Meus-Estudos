#! python

class Humano:
    # atributo de classe
    # esse atributo de Classe é compartilhado por todas as instâncias
    especie = "Homo sapiens"

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):  # método Get pra ler
        return self._idade

    @idade.setter
    def idade(self, idade): # método set pra escrever/alterar
        if idade < 0:  # validação
            raise ValueError('Idade deve ser um número positivo')
        self._idade = idade

    def das_cavernas(self):
        # mesmo self.especie tendo o mesmo nome do atributo da Classe, ele prevalece.
        self.especie = "Homo Neanderthalensis"
        return self  # chamando o mesmo objeto/instancia

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple('Homo ' + adj for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Nearderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    jose.idade = 40
    print(f'Nome: {jose.nome}, Idade: {jose.idade}')
