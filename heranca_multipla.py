#! python

# HERANÇA MULTIPLA
class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):  # class Homem herda da class Animal
    @property
    def capacidades(self):
        return super().capacidades + ('Amar', 'falar', 'estudar')


class Aranha(Animal):  # class Aranha herda de  class Animal
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teias', 'andar pelas paredes')


class HomemAranha(Aranha, Homem):  # class HomemAranha herda da class Aranha e da class Homem
    @property
    def capacidades(self):
        return super().capacidades + \
            ('bater em bandidos', 'atirar teias entre prédios')


if __name__ == '__main__':
    john = Homem()
    print(f'john: {john.capacidades}')

    aranha = Aranha()
    print(f'aranha: {aranha.capacidades}')

    peter = HomemAranha()
    print(f'peter: {peter.capacidades}')
