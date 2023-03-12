pmb = pc = pt = 0
npmb = ':P'

print(30 * '-')
print('      LOJA SUPER BARATÃO')
print(30 * '-')

while True:
    np = input('Nome do produto: ')
    pp = float(input('Preço: R$'))

    o = 'a'
    while o not in 'sn':
        o = input('Deseja continuar? [S/N] ').strip().lower()[0]

    if pp > 1000:
        pc += 1
    pt += pp

    if pmb == 0 or pmb > pp:
        pmb = pp
        npmb = np

    if o == 'n':
        break

print(7 * '-', 'FIM DO PROGRAMA', 7 * '-')
print(f'O total da compra foi R${pt:.2f}\nTemos {pc} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {npmb} que custa R${pmb:.2f}')
