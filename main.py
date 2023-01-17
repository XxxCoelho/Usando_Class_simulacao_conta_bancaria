from cliente import Cliente
from cc import ContaCorrente
from cp import ContaPoupanca


class Banco:

    def __init__(self):
        self.agencia = 63007
        self.conta = 1233216
        self.cliente = None

    def adicionar_cliente(self, cliente):
        self.cliente = cliente
        if not cliente.conta:
            print(f'Sr(a).{cliente.nome} não possui conta nenhuma')
            return
        else:
            if self.agencia != cliente.conta.agencia:
                cliente.conta.acessar = False
                print(f'{cliente.nome} não é nosso cliente! Faça uma conta!')
                return
            print('Bem-vindo!')
            return

    def criar_conta(self, conta=None, cliente=None):
        if self.cliente is None:
            self.cliente = cliente

        self.cliente.conta = conta(agencia=self.agencia, conta=self.conta, nome=self.cliente.nome)


Airton = Cliente('Airton Coelho', 22)
BB = Banco()
BB.adicionar_cliente(Airton)
BB.criar_conta(ContaPoupanca)

BB.cliente.conta.depositar(1000)
BB.cliente.conta.sacar(250)
BB.cliente.conta.extrato()