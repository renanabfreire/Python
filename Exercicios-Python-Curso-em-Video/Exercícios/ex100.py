# Importando gerador de valor aleatório
from random import randint
from time import sleep

# Adicionando valores
numeros = []


# Função para sorteio e formação da lista
def sorteio():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        n = randint(0, 10)
        print(n, end=' ', flush=True)  # Escrevendo
        sleep(0.3)  # pausa
        numeros.append(n)  # Adicionando valor à lista
    print('PRONTO!')

# Função para soma dos pares
def somapar():
    pares = 0
    for c in numeros:
        if c % 2 == 0:  # Conferindo se é par
            pares += c  # Somando
    # Devolvendo
    print(f'Somando os valores pares de {numeros}, temos {pares}')


# Programa principal
sorteio()
somapar()
