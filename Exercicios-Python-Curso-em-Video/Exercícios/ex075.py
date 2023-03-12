t = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))

print(f'Você digitou os valores {t}')
print(f'O valor 9 apareceu {t.count(9)} vezes')

if 3 in t:
    print(f'O valor três apareceu na {t.index(3) + 1}ª posição')

else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares foram: ', end='')
for cont in t:
    if cont % 2 == 0:
        print(cont, end=' ')
