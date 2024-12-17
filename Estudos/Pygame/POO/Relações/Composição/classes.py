class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.materias = []

    def adicionarcadeira(self, nome, carga):
        self.materias.append(Cadeira(nome, carga))

    def listar_materias(self):
        print(f'O aluno {self.nome}, cursa:')
        for materia in self.materias:
            print(f'{materia.nome} | {materia.carga}h')

    def __del__(self):
        print(f'{self.nome} foi apagado')


class Cadeira:
    def __init__(self, nome, carga):
        self.nome = nome
        self.carga = carga

    def __del__(self):
        print(f'{self.nome} foi apagada')
