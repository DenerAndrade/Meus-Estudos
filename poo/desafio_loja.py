
from datetime import datetime
from loja import Vendedor, Cliente, Compra


def main():
    cliente = Cliente('Maria lima', 44)
    vendedor = Vendedor('Pedro Garrido', 34, 5000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra(cliente, datetime(2018, 6, 4,), 256)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)
    print(f'Total:{valor_total} em {qtde_compras} compras')
    print(f'Ultima compra: {cliente.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
