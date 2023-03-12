print('Digite 3 números!')

n1 = int(input('Primeiro: '))
n2 = int(input('Segundo: '))
n3 = int(input('Terceiro: '))

if n1 > n2 and n1 > n3:
        print(f'{n1} é o maior número!')

if n2 > n1 and n2 > n3:
        print(f'{n2} é o maior número!')

if n3 > n2 and n3 > n1:
        print(f'{n3} é o maior número!')

if n1 < n2 and n1 < n3:
        print(f'{n1} é o menor número!')

if n2 < n1 and n2 < n3:
        print(f'{n2} é o menor número!')

if n3 < n2 and n3 < n1:
        print(f'{n3} é o menor número!')
