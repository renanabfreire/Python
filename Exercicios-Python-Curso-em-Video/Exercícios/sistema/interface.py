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

def escrever(txt):
    print(30 * '-')
    print(txt.center(30))
    print(30 * '-')

def menu(opcs):
    escrever('MENU PRINCIPAL')
    cont=1
    for c in opcs:
        print(f'\033[33m{cont}\033[0m - \033[34m{c}\033[0m')
        cont += 1
    print(30 * '-')
