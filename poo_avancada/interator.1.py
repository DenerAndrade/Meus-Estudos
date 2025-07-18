class FeiraFrutas:
    def __init__(self, repeticoes=3):
        self.frutas = ['Pera', 'Goiaba', 'Abacaxi', 'Kiwi', 'Amora']
        self.indice = 0
        self.repeticoes = repeticoes
        self.cont_repeticoes = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.frutas) and self.indice <= self.repeticoes:
            self.cont_repeticoes = self.indice
            fruta = self.frutas[self.indice]
            self.indice += 1
            return fruta
        # if self.indice <= self.repeticoes:
        #     self.cont_repeticoes = self.indice
        #     self.cont_repeticoes += 1
        #     return fruta


diaFeira = FeiraFrutas(2)

for fruta in diaFeira:
    print(fruta)
