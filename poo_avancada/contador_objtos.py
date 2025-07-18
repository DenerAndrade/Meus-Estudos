class ClasseSimples:
    contador = 0  # Atributo de classe (compartilhado por todas as instâncias)

    def __init__(self):
        # ClasseSimples.contador += 1
        self.contar()

    @classmethod
    def contar(cls):
        cls.contador += 1


if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador)
