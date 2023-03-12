print('CONVERSOR')

ni = int(input('Digite o número para a conversão: '))
ne = int(input('Para conversão digite:\n1 para binário, 2 para octal e 3 para hexagonal:\n'))

if ne == 1:
    print(f'{ni} em binário é: \033[7m{bin(ni)[2:]}\033[m')
elif ne == 2:
    print(f'{ni} em octal é: \033[7m{oct(ni)[2:]}\033[m')
elif ne == 3:
    print(f'{ni} em hexagonal é: \033[7m{hex(ni)[2:]}\033[m')
else:
    print('Essa opção não existe. Tente novamente em outro momento')
