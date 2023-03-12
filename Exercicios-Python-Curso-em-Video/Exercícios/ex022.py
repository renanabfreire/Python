n = str(input('Digite seu nome completo: ')).strip()

print(n.upper())
print(n.lower())

d = n.split()
t = ''.join(d)

print(f'O nome possui {len(t)} letras')
print(f'Sendo {len(d[0])} no primeiro')
