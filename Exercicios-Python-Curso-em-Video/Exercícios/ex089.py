# Importação de módulos
from time import sleep

# criando lista dos alunos
listageral = []  # Lista do final
dadosdoaluno = []  # Dados temporarios

n = -1

print('-=' * 15)
print(f'{"ORGANIZE AS NOTAS":^30}')
print('-=' * 15)

# Criando repetição
while True:
    # Recebendo dados
    dadosdoaluno.append(input('Digite o nome do aluno: '))  # Nome
    dadosdoaluno.append(float(input('Primeira nota: ')))  # Primeira nota
    dadosdoaluno.append(float(input('Segunda nota: ')))  # Segunda nota

    listageral.append(dadosdoaluno[:])
    dadosdoaluno.clear()

    # Dando encerramento ou continuação ao laço
    o = ' '
    while o not in 'SsNn':
        o = input('Deseja continuar? [S/N] ').strip()[0]
    if o in 'Nn':
        break

print('-=' * 15)

# Tabela para organização
print(f'{"Nº":3}', end=' ')
print(f'{"Nome":14}', end=' ')
print(f'{"Média":4}')

print('-' * 30)

# Mostrando resultados
for i, c in enumerate(listageral):
    print(f'{i+1:0>3}.', end=' ')
    print(f'{c[0]:14}', end=' ')

    media = (c[1]+c[2])/2  # Calculando média

    # Dando cores para aprovados ou reprovados
    if media >= 7:
        print(f'\033[32m{media:.2f}\033[m')
    else:
        print(f'\033[31m{media:.2f}\033[m')

# Nota particular
while True:
    n = int(input('Mostrar notas de qual aluno? [0 para parar] '))
    if n == 0:
        break
    print(f'Notas de {listageral[n - 1][0]} são {listageral[n - 1][1:]}')
    print('-' * 30)

print('FINALIZANDO...')
sleep(0.5)
print('<<< PROGRAMA ENCERRADO >>>')
