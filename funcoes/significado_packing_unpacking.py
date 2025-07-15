# Packing recebe os valores restantes

a, *b = 1, 2, 3, 4  # a variavel '*b' recebe os valores restantes

print(a)
print(b)  # a variavel '*b' recebe os valores restantes


# Unpacking em uma função
def soma(a, b, c):
    return a + b + c


valores = [1, 2, 3]
resultado = soma(*valores)  # Expande os valores da lista em argumentos
print(resultado)  # Saída: 6


# Unpacking com Dicionários e **
# Com dicionários, o operador ** expande pares de chave-valor.

# Exemplo:

def mostrar_dados(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")


dados = {"nome": "João", "idade": 25}
mostrar_dados(**dados)  # Expande o dicionário em argumentos nomeados
# Saída: Nome: João, Idade: 25


# Resumo:

# Packing: Agrupa múltiplos valores em uma coleção.
# Unpacking: Extrai valores de uma coleção para variáveis individuais.
# * e **: Facilitam packing e unpacking em listas e dicionários, respectivamente.
# Esses conceitos são muito úteis para escrever código mais limpo e dinâmico.
