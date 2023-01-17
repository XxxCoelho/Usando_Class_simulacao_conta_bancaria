from abc import ABC, abstractmethod
from utilitarios import organizar


class Conta(ABC):

    def __init__(self, agencia, conta, nome):
        super().__init__()
        self.__agencia = agencia
        self.__conta = conta
        self._saldo = 0
        self.nome = nome
        self.acessar = True

    @abstractmethod
    def sacar(self, valor):
        pass

    @property
    def agencia(self):
        return self.__agencia

    @property
    def conta(self):
        return self.__conta()

    @conta.setter
    def conta(self, valor):
        if isinstance(valor, (str, float)):
            valor = int(valor.replace('.', '').replace(',', '').replace('-', ''))
        self.__conta = valor

    @agencia.setter
    def agencia(self, valor):
        if isinstance(valor, (str, float)):
            valor = int(valor.replace('.', '').replace(',', '').replace('-', ''))
        self.__agencia = valor

    def extrato(self):
        if self.acessar:
            print(f'Nome {self.nome}')
            print(f'Agencia {organizar(self.__agencia, "A")}')
            print(f'Conta {organizar(self.__conta, "C")}')
            print(f'Saldo R${self._saldo:.2f}')
            print()
            return
        print(f'Sr(a).{self.nome} não tem acesso a conta')

    def depositar(self, valor):
        if self.acessar:
            if isinstance(valor, str):
                valor = round(float(valor.replace(',', '.').replace('R$', '').strip()), 2)
            self._saldo += valor
            self.extrato()
            return
        print(f'Sr(a).{self.nome} não pode depositar')
