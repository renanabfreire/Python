print('Hello World!')

from pessoa import Pessoa

p1 = Pessoa('Luiz', 17)
p2 = Pessoa('joão', 17, True, False)

print(p1)
print(p2)

p1.nome = 'Renan'

p1.falar('joguinhos')
p1.pararfalar()

print(p1.nome)
print(p2.nome)

p1.comer('maçã')
p1.falar('POO')
p1.pararcomer()
p1.falar('POO')
p1.comer('pizza')
p1.pararfalar()
p1.comer('pizza')
