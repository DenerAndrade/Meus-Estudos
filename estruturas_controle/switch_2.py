# def get_tipo_dia(dia):
#     dias = {
#         1: 'Fim de semana',
#         2: 'Dia de semana',
#         3: 'Dia de semana',
#         4: 'Dia de semana',
#         5: 'Dia de semana',
#         6: 'Dia de semana',
#         7: 'Fim de semana',

#     }
#     return dias.get(dia, '** Invalido**')


# if __name__ == '__main__':
#     for dia in range(8):
#         print(f'{dia}: {get_tipo_dia(dia)}')


def get_tipo_dia(dia): # ESTRUTURA MATCH CASE IGUAl A SWITCH CASE
    match dia:
        case 2 | 3 | 4 | 5 | 6:
            return 'Dia de semana'
        case 1 | 7:
            return 'Fim de semana'
        case _:
            return '** inválido **'


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {get_tipo_dia(dia)}')
