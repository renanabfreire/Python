print('Digite 3 retas para ver se formam um triângulo: ')

r1 = float(input('Primeira reta mede: '))
r2 = float(input('Segunda reta mede: '))
r3 = float(input('Terceira reta mede: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, elas formam um triângulo')

    if r1 == r2 == r3:
        print('E esse é um triângulo equilátero!')
    elif r1 != r2 != r3 and r1 != r3:
        print('E esse é um triângulo escaleno')
    else:
        print('E esse é um triângulo isóceles')

else:
    print('Não, elas não formam um triângulo!')
