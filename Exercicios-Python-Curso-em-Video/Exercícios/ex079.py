l = []

while True:
    n = int(input('Digite um valor: '))

    if n not in l:
        l.append(n)
        print('Valor adicionado com sucesso...')
    
    else:
        print('Valor duplicado! Não vou adicionar...')
    
    o = ' '
    while o not in 'sn':
        o = input('Deseja continuar? [S/N] ').lower()[0]

    if o == 'n':
        break

l.sort()

print(20 * '-=')
print(f'Você digitou os valores {l}')
