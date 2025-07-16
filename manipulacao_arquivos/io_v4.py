
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
# except IndexError:
#     pass
finally:
    print('Finally')
    arquivo.close()


if arquivo.closed:
    print('O arquivo foi fechado')
