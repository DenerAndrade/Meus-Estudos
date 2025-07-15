produto = {'nome': 'Caneta chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto: # acessando chave 
    print(chave)

for valor in produto.values():  # acessando o valor do dicionario
    print(valor)

for chave, valor in produto.items():  # acessando chave e valor ao mesmo tempo
    print(chave, '=', valor)
