print('Descubra como ficará o seu salário!')

s = float(input('Digite o seu salário atual em reais: \nR$'))

if 1250 < s:
    a = s / 100 * 10
    print('Seu salário reajustado será de R${:.2f}'.format(s + a))
else:
    a = s / 100 * 15
    print('Seu salário reajustado será de R${:.2f}'.format(s + a))
