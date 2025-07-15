def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a, b, c')  # *args / packing
    # *args/posicional 'a, b, c'  /// kwargs/nomeados ' legal=True, valor=12.98
    todos_params('a, b, c', legal=True, valor=12.98)
    # *args/posicional 'Ana, False,{ 1, 2, 3} /// kwargs/noemados ' tamanho='M', sapato=39'
    todos_params('Ana', False, {1, 2, 3}, tamanho='M', sapato=39)
    todos_params(primeiro='joao', segundo='Maria')

    # Não é possivel chamar *args/posicionais/packing depois de ter chamado Kwargs/noemados/unpacking
    # EXEMPLO de que não é possivel:
    # todos_params(primeiro='Thiago', 'Carlos')
