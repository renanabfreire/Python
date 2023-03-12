q = int(input('Você deseja a tabuada de qual número inteiro? \n'))

print('-' * 12)

for c in range(1, 11):
    print('{} x {:2} = {}'.format(q, c, q * c))

print('-' * 12)
