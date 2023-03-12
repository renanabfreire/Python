def escreva(txt):
    tam = len(txt) + 2
    print(tam * '-')
    print(f' {txt}')
    print(tam * '-')


def cor(n):
    print(f'\033[{n}m')


com = 'start'
while True:
    cor(43)
    escreva('SISTEMA DE AJUDA PyHELP')
    cor(0)
    com = input('função ou Bivblioteca > ')
    if com == 'FIM!':
        break
    cor(46)
    escreva(f'Acessando o manual do comando {com}')
    cor(47)
    h = help(com)
