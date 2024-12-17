from pessoa import Pessoa

# Criando normal
p1 = Pessoa('Renan', 17)
print(p1.idade, '\n', p1.get_ano_nascimento())

# Criando por meio de classe para valores da classe
p2 = Pessoa.por_ano_nascimento('João', 2002)
print(p2.idade, '\n', p2.get_ano_nascimento())
