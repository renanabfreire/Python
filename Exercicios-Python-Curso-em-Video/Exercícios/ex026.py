f = str(input('Digite uma frase: ')).strip().lower()

na = f.count('a')
p1 = int(f.find('a'))
p2 = f.rfind('a')

print(f'A letra A aparece {na} na frase.')
print(f'A primeira aparece na posição {p1 + 1}')
print(f'A última aparece na posição {p2 + 1}')
