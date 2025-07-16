# with de forma automatica fecha o arquivo sem ter a necessidade de chamar..
# arquivo.close()
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('O arquivo foi fechado')
