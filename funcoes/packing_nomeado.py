# **kwargs
# **kwargs: captura argumentos nomeados em um dicionário,....
# permitindo o uso de .items() para iterar pelas chaves e valores.


# !!!!! *args: captura argumentos posicionais em uma tupla. !!!

# **kwargs: captura argumentos nomeados em um dicionário,....
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='L. hamilton',
                 segundo='M. Verstapen',
                 terceiro='S. vettel',
                 quarto='F. Alonso')
