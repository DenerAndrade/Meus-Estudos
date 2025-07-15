class Usuario:
    cargo = 'usuario'
    nota = '9'

    def __init__(self, nome, idade):
        # self.altura = altura
        self.altura = '173'

# Quando coloco esse descorador @classmethod em cima de um método,
# estou afirmando ao python  que esse não é mais um método de instância,
# e sim um método de Classe.
    @classmethod
    def cargo_usuario(cls):
        print(cls.cargo)


    @staticmethod
    def e_adulto(idade):
        if idade >= 18:
            print('sou maoir de Idade')
        else:
            print('sou menor de Idade')
                

# tenho acesso aos atributos de classe através do método de classe
# Usuario.cargo_usuario()
Usuario.e_adulto(17)
