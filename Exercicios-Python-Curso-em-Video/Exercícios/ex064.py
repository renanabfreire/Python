n = s = c = 0

print('Digite qualquer valor abaixo para soma e digite 999 para encerrar')

while n != 999:

    n = int(input(f'Valor {c + 1}: '))

    if n != 999:

        s += n
        c += 1


print(f'Você selecionou {c} números e a soma é de {s}.')
