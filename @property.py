# EXEMPLO DE @PROPERTY


class Terreno:
    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    @property
    def area(self):
        return self.largura * self.comprimento


t = Terreno(10, 20)
print(f"Largura: {t.largura} m")
print(f"Comprimento: {t.comprimento} m")
# por conta do @property consigo chamar o método (t.area ) sem precisar colocar parênteses  t.area()
print(f"Area: {t.area} m²")
