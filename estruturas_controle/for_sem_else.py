PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    found = False  # .split() separa os espaços em brancos
    for palavra in texto.lower().split():  # .lower() colocar palavras em minúsculas
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos 1 palavra proibida: ', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado: ', texto)
