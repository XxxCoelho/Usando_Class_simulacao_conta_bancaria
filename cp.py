from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, nome):
        super().__init__(agencia, conta, nome)

    def sacar(self, valor):
        if self.acessar:
            if self._saldo <= 0:
                print("Saldo insuficiente")
                return
            self._saldo -= valor
            print(f'Saque R${valor:.2f} realizado!')
