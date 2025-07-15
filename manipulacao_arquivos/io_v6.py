#! python
# with de forma automatica fecha o arquivo sem ter a necessidade de chamar..
# arquivo.close()
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('O arquivo foi fechado')

if saida.closed:
    print('O arquivo de Saida já foi fechado')
