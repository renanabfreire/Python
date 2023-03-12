c = 10

v = int(input('Digite valor inicial da PA: '))
r = int(input('Digite a razão da PA: '))

while c != 0:

    print(v, end=' ')

    v += r

    c -= 1
    if c == 0:
        c = int(input('\nQuantos valores a mais você gostaria de ver? '))

print('\nEspero ter ajudado!')
