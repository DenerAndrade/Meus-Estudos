

def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante: Cindição de parada
    # retorne sequencia SE|if o tamanho|len da sequencia for exatamente igual
    # a quantidade caso contrario|else chame de novo a função|def fibonacci
    # passando os mesmo parametros
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 20 primeiros números
    for fib in fibonacci(20):
        print(fib)
