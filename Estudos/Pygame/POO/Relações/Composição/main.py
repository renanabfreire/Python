from classes import Aluno

a1 = Aluno('Renan', 17)
a1.adicionarcadeira('Programação Orientada a Objetos', 60)
a1.adicionarcadeira('Pesquisa Aplicada à Ciência de Dados', 45)

a2 = Aluno('Luiz', 21)
a2.adicionarcadeira('Banco de Dados', 60)
a2.adicionarcadeira('Estrutura de Dados', 120)
a2.adicionarcadeira('Metodologia do Trabalho Científico', 45)

a1.listar_materias()
print()
a2.listar_materias()

print('#'*20)
