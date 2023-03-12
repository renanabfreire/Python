from datetime import date

a = date.today().year

print('Descubra seu tempo para o alistamento')

b = int(input('Digite o ano do seu nascimento: '))
i = a - 18

if b > i:
    if b - i == 1:
        print(f'Ainda não chegou o seu momento, mas falta {b - i} ano')
    else:
        print(f'Ainda não chegou o seu momento, mas faltam {b - i} anos')
elif b < i:
    if i - b == 1:
        print('Que atraso, já passou 1 ano do seu alistamento obrigatório')
    else:
        print(f'Que atraso, já passou {i - b} anos do seu alistamento obrigatório')
elif b == i:
    print('Não atrase, chegou a hora de prestar serviço ao seu país!')
