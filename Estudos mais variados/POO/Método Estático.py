from pessoa import Pessoa

# Usando função com objeto
p1 = Pessoa('Renan', 17)
print(p1.gera_id())

# Usando função sem objeto
print(Pessoa.gera_id())
