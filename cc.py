from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, nome, limite=100):
        super().__init__(agencia, conta, nome)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if self.acessar:
            if (self._saldo + self.limite) < valor:
                print(f"Saldo insuficiente")
                return
            self._saldo -= valor
            print(f'Saque R${valor:.2f} realizado!')
