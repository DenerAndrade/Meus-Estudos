#! python

class Humano:
    # atributo de classe
    # esse atributo de Classe é compartilhado por todas as instâncias
    especie = "Homo sapiens"

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def inteligente(self):
        raise NotImplementedError('Propriedade não esta implementada.')

    @property
    def idade(self):  # método Get pra ler
        return self._idade

    @idade.setter
    def idade(self, idade):  # método set pra escrever/alterar
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

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    anonimo = Humano('John')

    try:
        print(anonimo.inteligente)
    except NotImplementedError:
        print('Propriedade Abstrata')


jose = HomoSapiens('Jose')
print(f'{jose.nome} da classe {jose.__class__.__name__}, inteligente {jose.inteligente}')

gronh = Nearderthal('Gronh')
print(f'{gronh.nome} da classe {gronh.__class__.__name__}, inteligente {gronh.inteligente}')
