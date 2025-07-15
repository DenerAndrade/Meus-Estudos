def get_tipo_dia(dia): # def é um função
    dias = {
        (1, 7): 'Fim de Semana', # tupla
        tuple(range(2, 7)): 'Dia da Semana'  # tupla
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** Dia Invalido **') # Generator


if __name__ == '__main__':
    for dia in range(0, 13):
        print(f'{dia}: {get_tipo_dia(dia)}') # f de interpolação
