a = 0
b = 1

n = int(input('Quantidade de valores da Sequência de Fibonacci: '))

while n != 0 and n != -1:
    print(a, end=' ')

    if n != 1:
        print(b, end=' ')

    a += b
    b += a

    n -= 2
