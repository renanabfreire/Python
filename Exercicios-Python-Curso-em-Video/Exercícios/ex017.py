from math import hypot

co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
hi = hypot(co, ca)

print('A hypotenusa mede {:.3f}'.format(hi))
