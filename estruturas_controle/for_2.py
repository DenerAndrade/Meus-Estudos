# Palavra = 'Paralelepipedo'
# # para cada letra na Variável Palavra (imprima a cada letra)
# for letra in Palavra:
#     print(letra)  # imprime a letras uma embaixo da outra

# Palavra = 'Paralelepipedo'
# # para cada letra na Variável Palavra (imprima a cada letra)
# for letra in Palavra:
#     # imprime as letras lado a lado separando com virgula P,a,r,a,l,e,l,e,p,i,p,e,d,o,
#     print(letra, end=',')

#  ------- LISTAS --------
Aprovados = ['Rafaela', 'Pedro', 'Maria', 'Carlos', 'Roberto']
for nome in Aprovados:
    print(f'nome: {nome}')

# Para cada posição na variável (nome) dentro da variável Aprovados  ENUMERE cada uma delas
for posicao, nome in enumerate(Aprovados):
    # posição + 1 é para iniciar com o numeo 1 e não com o numero  0
    print(f'{posicao + 1})', nome)

# ----------- TUPLAS ---------------

dias_semana = ('Segunda', 'Terca', 'Quarta', 'Quinta'
               'Sexta', 'Sabado', 'Domingo')
for dia in dias_semana:
    print(f'Hoje é dia: {dia}')

# ------- SET CONJUNTO -------------

for letras in set('muito legal'):  # conjuto não garante ordenação
    print(letras)
