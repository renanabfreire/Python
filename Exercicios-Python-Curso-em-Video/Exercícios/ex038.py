print('Descubra o maior entre dois valores')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print(f'{n1} é o maior valor!')
elif n2 > n1:
    print(f'{n2} é o maior valor!')
elif n1 == n2:
    print('Não há valor maior')
