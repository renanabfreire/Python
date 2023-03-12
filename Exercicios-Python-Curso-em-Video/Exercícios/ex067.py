while True:
    print(22 * '-')
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(22 * '-')

    if n < 0:
        break

    for c in range(1, 11):
        print('{} x {:2} = {}'.format(n, c, n * c))
