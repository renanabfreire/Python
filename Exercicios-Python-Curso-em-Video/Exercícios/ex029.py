from math import trunc

v = float(input('Digite a velocidade do seu veículo em km/h: '))

if v > 80:
    m = trunc(v - 80) * 7
    print('Você foi multado por ultrapassar o limite de 80Km/h!')
    print('Você deverá pagar R${:.2f}'.format(m))
else:
    print('Tenha um bom dia! Dirija com segurança!')