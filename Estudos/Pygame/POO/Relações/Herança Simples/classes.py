class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.dados = []

    def acessarsistema(self):
        print(f'{self.nome} acessou o sistema da escola')


class Estudante(Pessoa):
    def adicionar_nota(self, materia, nota):
        self.dados.append([materia, nota])

    def receber_nota(self):
        print(f'Notas de {self.nome}')
        for i in self.dados:
            print(f'{i[0]:<20}: {i[1]:>5.2f}')


class Professor(Pessoa):
    def postar_nota(self, aluno, nota):
        self.dados.append([aluno, nota])

    def listaalunos(self):
        for aluno in self.dados:
            print(f'{aluno[0]:<20}: {aluno[1]:>5.2f}')
