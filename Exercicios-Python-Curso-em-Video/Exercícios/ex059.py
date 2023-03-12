e = 4
n1 = 0
n2 = 0

while e != 5:
    if e == 4:
        n1 = int(input('Digite valor 1: '))
        n2 = int(input('Digite valor 2: '))

    if e == 1:
        print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}\n')

    if e == 2:
        print(f'A multiplicação entre {n1} e {n2} é igual a {n1 * n2}\n')
    if e == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}\n')
        elif n2 > n1:
            print(f'O maior valor é {n2}\n')
        else:
            print('Os valores são iguais\n')

    e = int(input('Operações:\n(1)Soma\n(2)Multiplicação\n(3)Mostrar Maior\n(4)Novos valores\n(5)Fechar programa\n'
                  'Opção Desejada: '))

print('Espero ter ajudado!')
