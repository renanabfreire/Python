n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
print('A soma vale {}, a subtração vale {}, a multiplicação vale {} e a divisão vale {} \n Além disso a raíz é igual '
      'a {} e a potência é {}'.format(s, sub, m, d, n1 ** (1 / n2), n1 ** n2))
print('A divisão tabem pode ser {} com resto {}'.format(n1 // n2, n1 % n2))
