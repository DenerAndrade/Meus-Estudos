from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

# com essa função nâo é mais necessario colocar casa.tarefas e mercado.tarefas
    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possivel IndexError
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendentes())'


class Tarefa:
    # CONSTRUTOR
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.craicao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao}' + ' '.join(status)


def main():
    casa = Projeto('Tarefas da Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Levar o lixo', datetime.now() + timedelta(days=3))
    print(casa)

    casa.procurar('Passar roupa').concluir()
    # for tarefa in casa.tarefas:
    for tarefa in casa:
        print(f'-{tarefa}')
    print(casa)

    mercado = Projeto('Compras no Mercado')
    mercado.add('Tomate')
    mercado.add('Cebola')
    mercado.add('Carne')
    mercado.add('Pepino')
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    # for tarefa in mercado.tarefas:
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == "__main__":
    main()
