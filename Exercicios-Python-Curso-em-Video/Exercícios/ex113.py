def leiaint(txt):
    num = 0
    while True:
        try:
            num = int(input(txt))
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            break
    return num
        

def leiafloat(txt):
    num = 0
    while True:
        try:
            num = float(input(txt))
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            break
    return num


i = leiaint('Digite um inteiro: ')
p = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {p}.')
