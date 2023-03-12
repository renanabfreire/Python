print(12 * '=' + '\033[30mDescubra se seu empréstimo será aprovado!\033[m' + 12 * '=')
v = float(input('Qual o valor da casa em questão? R$'))
s = float(input('De quanto é o seu salário? R$'))
a = float(input('Em quantos anos você planeja quitar a compra? '))

ps = 30 * s / 100
vp = v / (a * 12)

if vp < ps:
    print('\n\033[32mSeu empréstimo será aprovado com parcelas de R${:.2f}! Aproveite!\033[m'.format(vp))
else:
    print('\n\033[31mSeu empréstimo não foi aprovado! aceitamos valores de até \033[32mR${:.2f}\033[31m, porém o sua '
          'parcela atingiu \033[7mR${:.2f}\033[0;31m.\033[m'.format(ps, vp))

print(19 * '=' + '\033[030mObrigado por nos consultar!\033[m' + 19 * '=')
