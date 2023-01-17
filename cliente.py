from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = None

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        if self._conta:
            print("Conta já criada!")
            return
        self._conta = conta
        print('Conta criada')
