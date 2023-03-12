from datetime import datetime
from random import randint


class Pessoa:
    anoatual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esté comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def pararcomer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        elif self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'Pessoa está falando sobre {assunto}.')
        self.falando = True

    def pararfalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def get_ano_nascimento(self):
        return self.anoatual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.anoatual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        return randint(1000, 9999)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nom):
        self._nome = nom.title()
