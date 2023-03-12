c = a = b = M = m = s = 0
q = 's'

while q == 's':
    a = int(input('Digite valor inteiro: '))
    q = input('Deseja continuar?[S/N] ').strip().lower()[0]

    if a > b:
        M = a
    elif a < b:
        m = a

    if m == 0:
        m = a

    b = a
    s += a
    c += 1

print(f'Você escolheu {c} números inteiros\n'
      f'A média entre eles foi {s / c}\n'
      f'O maior número foi {M}\n'
      f'E o menor {m}')
