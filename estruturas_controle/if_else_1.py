# Conceito    Nota
# A           De 10,0 à  9,1
# A-          De 9,0  à  8,1
# B           De 8,0  à  7,1
# B-          De 7,0  à  6,1
# C           De 6,0  à  5,1
# C-          De 5,0  à  4,1
# D           De 4,0  à  3,1
# D-          De 3,0  à  2,1
# E           De 2,0  à  1,1
# E-          De 1,0  à  0,0

# Para nota maiores que 10 e menos  que 0 será impresso "Nota Invalida"

def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'Nota invalida!'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota Invalida'


if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    # Variável conceito recebe o valor digitado no input e já convertido
    conceito = nota_conceito(valor_informado)
    print(conceito)
