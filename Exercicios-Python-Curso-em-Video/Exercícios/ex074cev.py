from random import randint

n = (randint(0, 9), randint(0, 9), randint(0, 9),
     randint(0, 9), randint(0, 9),)

print(f'Os valores sorteados foram: ', end='')

for v in n:
    print(v, end=' ')

print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
