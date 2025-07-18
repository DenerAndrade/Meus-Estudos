from datetime import date


class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def dias_vividos(self):
        return (date.today() - self.data_nascimento).days

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        print(f"Chamando o setter com: {value}")
        if not isinstance(value, date):
            raise ValueError("data_nascimento deve ser do tipo date")
        self._data_nascimento = value


p = Pessoa('Dener', date(1995, 2, 18))
print(p.dias_vividos())
