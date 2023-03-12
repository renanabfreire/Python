print('Descubra o valor a ser pago sabendo que o aluguel custa R$60 por dia e R$0,15 por km rodado:')

d1 = int(input('Quantidade de dias: '))
d2 = float(input('Quantidade de Km rodados: '))
p = (d1 * 60) + (d2 * 0.15)

print('Visto que em {} dias você percorra {}km, você deverá pagar R${:.2f}'.format(d1, d2, p))
