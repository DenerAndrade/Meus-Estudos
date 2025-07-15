#! python
from datetime import datetime, timedelta


class TarefaNãoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

# com essa função nâo é mais necessario colocar casa.tarefas e mercado.tarefas
    def __iter__(self):
        return self.tarefas.__iter__()

# Sobrecarga do operador
# projeto += tarefa
#
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        try:
            # Possivel IndexError
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao == descricao][0]
        except IndexError as e:
            raise TarefaNãoEncontrada(str(e))

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
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa


def main():
    casa = Projeto('Tarefas da Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Levar o lixo', datetime.now() + timedelta(days=3))
    casa += TarefaRecorrente('Trocar lencois', datetime.now(), 7)
    casa.procurar('Trocar lencois').concluir()
    print(casa)

    try:
        casa.procurar('Lavar prato - ERRO').concluir()
    except TarefaNãoEncontrada as e:
        print(f'A causa foi "{str(e)}"!')
    finally:
        print('"finally" Sempre sera executado')    

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
