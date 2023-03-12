print('Digite 3 retas para ver se formam um triângulo: ')

r1 = float(input('Primeira reta mede: '))
r2 = float(input('Segunda reta mede: '))
r3 = float(input('Terceira reta mede: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, elas formam um triângulo!')

else:
    print('Não, elas não formam um triângulo!')
