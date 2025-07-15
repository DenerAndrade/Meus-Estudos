#EXEMPLO DE @PROPERTY

class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    @property
    def idade(self):
        from datetime import date
        hoje = date.today()
        return hoje.year - self.nascimento


p = Pessoa("Ana", 1990)
print(p.nome)       # Ana
# por conta do @property consigo chamar o método (p.idade ) sem precisar colocar parênteses  p.idade()
print(p.idade)      # 2025 - 1990 = 35 (por exemplo)
