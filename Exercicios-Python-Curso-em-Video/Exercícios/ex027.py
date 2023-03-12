n = str(input('Digite seu nome completo: ')).title().split()

p = len(n)
ln = n[p - 1]

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {ln}')
