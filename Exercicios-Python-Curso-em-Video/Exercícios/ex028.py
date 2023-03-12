from random import choice
from time import sleep

ns = str(input('Adivinhe um número entre 0 e 5: '))

n5 = ['0', '1', '2', '3', '4', '5']
np = choice(n5)

print('Hmmmm...')
sleep(2)

if ns == np:
    print(f'Exatamente! o sorteado foi {np}')
else:
    print(f'Na verdade... O sorteado foi {np} :/')
