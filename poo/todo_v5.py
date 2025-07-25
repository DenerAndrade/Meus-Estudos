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
        self.criacao = datetime.now()
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


class TarefaRecorrente(Tarefa):  # HERANÇA -> classe pai(Tarefa)
    def __init__(self, descricao, vencimento,  dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas da Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Levar o lixo', datetime.now() + timedelta(days=3))
    casa.tarefas.append(TarefaRecorrente('Trocar lencois', datetime.now()))
    casa.tarefas.append(casa.procurar('Trocar lencois').concluir())
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
