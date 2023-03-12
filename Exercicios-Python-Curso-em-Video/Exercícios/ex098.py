# Impotando sleep
from time import sleep

# Criando o contador


def contador(inicio, fim, passo):
    # Validando valores negativos
    if passo < 0:
        passo *= -1
    # Validando 0
    if passo == 0:
        passo += 1

    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    # Validando contagens regressas
    if fim < inicio:
        passo *= -1

    # Obtendo final real
    if fim > inicio:
        fim += 1
    elif fim < inicio:
        fim -= 1

    # Escrevendo valores
    for cont in range(inicio, fim, passo):
        print(cont, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))

contador(a, b, c)
