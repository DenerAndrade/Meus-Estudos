class Calc:
    def tabu(self):
        self.numeros = int(input('Digite um numero: '))
        if self.numeros > 0:
            print(f'{self.numeros}Numero positivo')
        elif self.numeros < 0:
            print(f'{self.numeros }'+'numero negativo')
        else:
            print('Zero')


if __name__ == '__main__':
    c = Calc()
    c.tabu()
