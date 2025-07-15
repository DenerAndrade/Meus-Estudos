# **kwargs
# **kwargs: captura argumentos nomeados em um dicionário,....
# permitindo o uso de .items() para iterar pelas chaves e valores.


# !!!!! *args: captura argumentos posicionais em uma tupla. !!!

def resultado_f1(primeiro, segundo, terceiro, quarto):
    print(f'1){primeiro}')
    print(f'2){segundo}')
    print(f'3){terceiro}')
    print(f'4){quarto}')


if __name__ == '__main__':
    podium = {'primeiro': 'L. hamilton',
              'segundo': 'M. Verstapen',
              'terceiro': 'S. vettel',
              'quarto': 'F. Alonso'}
resultado_f1(**podium)
