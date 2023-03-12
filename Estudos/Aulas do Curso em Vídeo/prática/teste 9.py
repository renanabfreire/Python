n1 = float(input('Digite primeira nota: '))
n2 = float(input('Digite segunda nota: '))
n3 = float(input('Digite terceira nota: '))

m = (n1 + n2 + n3) / 3

print('A sua média foi {:.2f}'.format(m))

if m >= 7.00:
    print('Você está aprovado, parabéns!')
else:
    print('Você está retido!')
