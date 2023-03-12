q = 0

for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        q += n

print(f'A soma dos pares é igual a {q}')
