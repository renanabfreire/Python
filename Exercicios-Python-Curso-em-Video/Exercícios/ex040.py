print(8 * '=' + 'Veja desempenho escolar' + 8 * '=')
n1 = float(input('\nDigite nota 1: '))
n2 = float(input('Digite nota 2: '))

if n1 > 10:
    n1 = 10
if n1 < 0:
    n1 = 0

if n2 > 10:
    n2 = 10
if n2 < 0:
    n2 = 0

m = (n1 + n2) / 2

if m >= 7:
    print('\nPARABÉNS!!!\nVocê foi aprovado com média {:.2f}!'.format(m))
elif 7 > m >= 5:
    print('\nVocê Ainda não foi aprovado.\nSua média foi de {:.2f} e você deverá fazer recuperação!'.format(m))
else:
    print('\nInfelizmente você está reprovado.\nSua média foi de {:.2f}'.format(m))
