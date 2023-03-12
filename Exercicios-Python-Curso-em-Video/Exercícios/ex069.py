pM = hc = Mm = 0

while True:
    print(29 * '-')
    print('     CADASTRE UMA PESSOA')
    print(29 * '-')

    i = int(input('Idade: '))
    s = 'a'
    while s not in 'mf':
        s = input('Sexo[M/F]: ').strip().lower()[0]

    print(29 * '-')

    o = 'a'
    while o not in 'sn':
        o = input('Quer continuar? [S/N] ').strip().lower()[0]

    if i > 17:
        pM += 1

    if s == 'm':
        hc += 1

    if s == 'f' and i < 20:
        Mm += 1

    if o == 'n':
        break

print(7 * '=' + 'FIM DO PROGRAMA' + '=' * 7)
print(f'Total de {pM} de maior\nAo todo temos {hc} homens cadastrados\nE temos {Mm} mulheres com menos de 20 anos.')
