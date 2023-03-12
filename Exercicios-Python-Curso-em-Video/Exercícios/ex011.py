print('Descubra quantos litros de tinta você precisa comprar para a sua parede!')
h = float(input('Altura da parede em metros: '))
l = float(input('Largura da parede em metros: '))
a = h * l

print(f'Sabendo que cada litro de tinta você consegue pintar 2m^2 e que sua parede possui {a}m^2')
print(f'você precisa de {a / 2} litros!')
