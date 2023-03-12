numeroextenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

p = int(input('Digite um número entre 0 e 20: '))
while p < 0 or p > 20:
    p = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {numeroextenso[p]}')
