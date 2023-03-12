def area(a, b):
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {a*b:.1f}m².')


print(' Controle de Terrenos')
print(22*'-')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)
