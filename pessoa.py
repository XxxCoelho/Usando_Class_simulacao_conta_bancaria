class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            valor = str(valor.capitalize().strip())
        if isinstance(valor, int):
            print(f'Digite seu nome!')
            valor = 'Desconhecido'
        self._nome = valor

    @idade.setter
    def idade(self, valor):
        if isinstance(valor, str):
            valor = int(valor)
        self._idade = valor

