from random import sample

n1 = input('Digite um nome: ')
n2 = input('Digite outro: ')
n3 = input('Digite mais outro: ')

print(f'A nova ordem será: {sample([n1, n2, n3],k=3)}')

'''Lista = [valores]'''
