from random import choice as s

print('Vamos jogar pedra, papel e tesoura!')

o = ('pedra', 'papel', 'tesoura')
a = s(o)

p = str(input('Digite sua opção: ')).strip().lower()

if a == 'pedra' and p == 'tesoura' or a == 'papel' and p == 'pedra' or a == 'tesoura' and p == 'papel':
    print(f'\nYEAH\n\033[7;31mEu venci!\033[0;38m Você escolheu {p} e eu {a}.')
elif a == p:
    print(f'\nValeu a tentativa,\n\033[34mNós empatamos\033[0;38m, também escolhi {a}')
else:
    print(f'\nDroga :/\n\033[7;32mVocê ganhou...\033[0;38m Eu escolhi {a}')
