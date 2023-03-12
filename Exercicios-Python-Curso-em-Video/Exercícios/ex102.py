def fatorial(n, show=False):  # Função para cálculo do fatorial
    '''-> Calcula o fatorial de um número.
    :parâmetro n: O número a ser calculado.
    :parêmetro show: (opcional) Mostrar ou não a conta.
    return: O valor do fatorial de um número'''
    valor = 1
    print(30 * '-')
    while n != 0:
        valor *= n
        if show == True:
            if n > 1:
                print(f'{n} x', end=' ')
            elif n == 1:
                print(f'{n} =', end=' ')
        n -= 1
    return valor


print(fatorial(5, show=True))
