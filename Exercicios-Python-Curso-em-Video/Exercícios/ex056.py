iM = 0
ig = 0
qm = 0
hM = 'inexistente'

for c in range(1, 6):
    print(f'Pessoa {c}')
    n = input('Nome: ')
    i = int(input('Idade: '))
    g = int(input('(1)Homem ou (2)Mulher: '))

    if g == 1 and i > iM:
        iM = i
        hM = n
    elif i == iM:
        hM = f'{hM} e {n}'

    if g == 2 and i < 20:
        qm += 1

    ig += i

print(f'A média de idade é de {ig // 5} anos.')
print(f'O homem mais velho é {hM}!')
print(f'Existem {qm} mulheres com menos de 20 anos.')
