# Dicionário dos dados:
dados = {}

# Coletando e adicionando chave ao dicionário
dados['Nome'] = input('Nome: ') #Nome
dados['Média'] = float(input(f'Média de {dados["Nome"]}: ')) #Média
if dados['Média'] >= 7: #Situação
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'

# Escrevendo resultados
for i, c in dados.items():
    print(f'{i} é igual a {c}')
