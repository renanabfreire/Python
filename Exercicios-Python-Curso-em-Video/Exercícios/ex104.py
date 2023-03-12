def leiaint(txt):
    while True:
        num = input(txt)
        if num.isnumeric():
            break
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return int(num)


print(30 * '-')
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
