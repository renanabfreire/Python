l = []

while True:
    l.append(int(input('Digite um valor: ')))

    o = ' '
    while o not in 'sn':
        o = input('Quer continuar? [S/N] ').strip().lower()[0]

    if o == 'n':
        break

print(15 * '-=')
print(f'Você digitou {len(l)} elementos.')

l.sort(reverse=True)

print(f'Os valores em ordem decrescente são {l}')

if 5 in l:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
