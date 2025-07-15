# range é um seguência de números com  intervalo
# exemplo: quero uma sequência de números com interlado, começa de 33 ao 48
# 33, 34, 35, 36 , 37 ,38 , 39, 40, 41, 42, 43, 44, 45, 46, 47, 48
def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de Idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Maior idade'
    elif idade >= 100:
        return 'Centenario'
    else:
        return 'Idade Invalida!'


if __name__ == '__main__':
    for idade in (17, 23, 44, 101, 0, -1):  # tupla
        print(f'{idade}: {faixa_etaria(idade)}')
