PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:

    for palavra in texto.lower().split():  # .lower() colocar palavras em minúsculas
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos 1 palavra proibida: ', palavra)

            break

    else:
        print('Texto autorizado: ', texto)
