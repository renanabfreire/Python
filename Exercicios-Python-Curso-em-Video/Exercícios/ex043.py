print(12 * '=' + 'CALCULO DE IMC' + 12 * '=')

a = float(input('\nDigite altura: '))
p = float(input('Digite peso: '))

imc = p / a ** 2

print('\nSeu imc é de \033[7m{:.2f}\033[0m'.format(imc))

if imc < 18.5:
    print('\n\033[31mVocê está abaixo do peso.\033[m')
elif 18.5 <= imc <= 25:
    print('\n\033[32mVocê está no peso ideal.\033[m')
elif 25 < imc <= 30:
    print('\n\033[31mVocê está na faixa de sobrepeso.\033[m')
elif 30 < imc <= 40:
    print('\n\033[31mVocê está na faixa de obesidade.\033[m')
elif imc > 40:
    print('\n\033[31mVocê está na faixa de obesidade mórbida.\033[m')
