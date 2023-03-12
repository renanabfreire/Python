f = 'Eu vou passar no ENEM'

print(f[3])
print(f[3:13])
print(f[:13])
print(f[17:])
print(f[::3])

print(f.upper().count('U'))
print(len(f))
print(f.replace('ENEM', 'concurso'))
print(f.split())

d = f.split()
print(d[4])
print(d[3][1])

print("""Analisar str
frase = termo
len(frase) -> quantos caracteres tem frase
frase.count('o') -> quantas vezes aparece o.
frase.count('o', x, y) -> quantas vezes aparece o de x a y(sem o y)
frase.find('nan') -> a posição do nan - mostranddo apenas a casa que começa
                     valor inexistente aparece na posição -1
'xyz' in frase -> se há xyz no termo
""")
