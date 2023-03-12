from random import randint

npc = randint(0, 10)
c = 1

print('Adivinhe em qual número estou pesando entre 0 e 10!')
nuser = int(input('Seu palpite: '))

while npc != nuser:
    if npc < nuser:
        nuser = int(input('Menos... Tente novamente: '))
    elif npc > nuser:
        nuser = int(input('Mais... Tente novamente: '))

    c += 1

print(f'Acertou! Foram necessárias {c} tentativas!')
