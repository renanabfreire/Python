from random import randint

c = 0

print(11 * '=-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print(11 * '=-')

while True:
    npc = randint(1, 10)
    ouser = ' '

    while ouser not in 'pií':
        ouser = input('Par ou Ímpar? [P/I] ').strip().lower()[0]
    nuser = int(input('Diga um valor: '))
    s = nuser + npc
    print(22 * '-')

    if s % 2 == 0:
        print(f'Você jogou {nuser} e o computador {npc}. Total de {s} DEU PAR')
        if ouser == 'i':
            break

    if s % 2 == 1:
        print(f'Você jogou {nuser} e o computador {npc}. Total de {s} DEU ÍMPAR')
        if ouser == 'p':
            break

    print(22 * '-')
    print('Você VENCEU!')

    c += 1

print(22 * '-')
print('Você PERDEU!')
print(11 * '=-')
print(f'GAME OVER! Você venceu {c} vezes.')
print(11 * '=-')
