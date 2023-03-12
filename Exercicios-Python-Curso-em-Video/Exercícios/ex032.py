from datetime import date

a = int(input('Digite o ano para descobrir se ele é bissexto: '))

if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'Sim, o ano {a} é bissexto!')
else:
    print(f'Não, o ano {a} não é bissexto!')
