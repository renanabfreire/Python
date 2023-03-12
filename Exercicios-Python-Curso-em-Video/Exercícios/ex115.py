from sistema.interface import *
from sistema.arquivo import *

arq = 'pessoas cadastradas.txt'
if not existe(arq):
    criar(arq)

while True:
    menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    o = leiaint('Sua opção: ')
    if o == 1:
        escrever('Lista de Pessoas Cadastradas')
        ler(arq)
    elif o == 2:
        escrever('Novo Cadastro')
        nome = input('Nome: ')
        idade = leiaint('idade: ')
        cadastrar(arq, nome, idade)
    elif o == 3:
        escrever('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: digite uma opção válida\033[m')
