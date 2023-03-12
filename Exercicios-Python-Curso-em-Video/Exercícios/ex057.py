g = str(input('Digite seu gênero (M) ou (F): ')).strip().upper()[0]

while g not in 'FM':
    print('Gênero não identificado')
    g = str(input('Tente novamente: ')).upper()

print('Vlw, flw :P')
