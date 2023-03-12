q = 0

print(30 * '=')
print('          BANCO RABF')
print(30 * '=')

v = int(input('Que valor você quer sacar? R$'))

while v - 50 >= 0:
    v -= 50
    q += 1
print(f'Total de {q} cédulas de R$50')

q = 0
while v - 20 >= 0:
    v -= 20
    q += 1
print(f'Total de {q} cédulas de R$20')

q = 0
while v - 10 >= 0:
    v -= 10
    q += 1
print(f'Total de {q} cédulas de R$10')

q = 0
while v - 1 >= 0:
    v -= 1
    q += 1
print(f'Total de {q} cédulas de R$1')

print(30 * '=')
print('Volte sempre ao BANCO RABF! Tenha um Bom Dia!')
