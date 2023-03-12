# Criando variáveis
pessoas = []
mulheres = []
dados = {}
idadetotal = 0

# Obtendo dados das pessoas
while True:
    dados['nome'] = input('Nome: ')
    dados['sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
    # Obtendo nome das mulheres
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])

    n = int(input('Idade: '))
    # Obtendo idade e geral para média
    dados['idade'] = n
    idadetotal += n

    # Adicionando dados à lista
    pessoas.append(dados.copy())
    dados.clear()

    o = ' '  # Encerrando repetição
    while o not in 'sn':
        o = input('Quer continuar: [S/N] ').strip().lower()[0]
    if o == 'n':
        break

# Devolvendo informações
print('-=' * 30)
print(f'- O grupo tem {len(pessoas)} pessoas.')  # Quantidade de pessoas
media = idadetotal / len(pessoas)  # Média de idade
print(f'- A média de idade é de {media} anos.')
# Escevendo nome das mulheres
print('- As mulheres cadastradas foram:', end=' ')
for c in mulheres:
    print(c, end=' ')
# Pessoas acima da média
print('\n- Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > media:
        for i, c in p.items():
            print(f'{i} = {c};', end=' ')
        print()
