d = ' '
n = int(input('Digite um valor inteiro: '))

for c in range(2, n):
    if n % c == 0:
        d = ' não '

print(f'o número{d}é primo!')
