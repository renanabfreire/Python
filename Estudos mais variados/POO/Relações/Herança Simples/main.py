from classes import Estudante, Professor

a1 = Estudante('Renan', 17)
a1.adicionar_nota('matemática', 10)
a1.adicionar_nota('gramática', 9.5)
a1.adicionar_nota('redação', 9.6)

a1.acessarsistema()
a1.receber_nota()

print()

p1 = Professor('Otávio', 45)
p1.acessarsistema()
p1.postar_nota('Gabriel', 5.2)
p1.postar_nota('João', 8.6)
p1.postar_nota('Renan', 7.5)
p1.postar_nota('Luiz', 9.8)
p1.listaalunos()
