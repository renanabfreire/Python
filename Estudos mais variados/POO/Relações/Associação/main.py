import classes as cl

e1 = cl.Escritor('Rodrigo')
e2 = cl.Escritor('João')
c = cl.Caneta('bic')
m = cl.MaquinaDeEscrever()

print(e1.nome)
print(c.marca)
m.escrever()

print()

# associação
e1.ferramenta = m
e2.ferramenta = c

e1.ferramenta.escrever()
e2.ferramenta.escrever()
