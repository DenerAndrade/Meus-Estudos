class Humano:
    # atributo de classe
    # esse atributo de Classe é compartilhado por todas as instâncias
    especie = "Homo sapiens"

    def __init__(self, nome):
        self.nome = nome

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
    gronk = Nearderthal('Gronk')
    print(f'Evolucao (a partir da classe):{", ".join(HomoSapiens.especies())}')
    print(f'Evolcao (a partir da Instancia): {", ".join(jose.especies())}')
    print(f'Homo Spiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Nearderthal.is_evoluido()}')
    print(f'jose evoluido ? {jose.is_evoluido()}')
    print(f'gronk evoluido ? {Nearderthal.is_evoluido()}')
