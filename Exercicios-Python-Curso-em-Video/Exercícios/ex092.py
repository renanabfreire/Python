# Importando data
from datetime import date

dados = {}  # Criando dicionério

# Obtendo dados
dados['Nome'] = input('Nome: ')

# Calculando idade
anodenascimento = int(input('Ano de nascimento: '))
n = date.today().year
dados['Idade'] = n - anodenascimento

# Obtendo ctps e definindo continuação
dados['Ctps'] = int(input('Carteira de trabalho: '))

if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = input('Salário: R$')
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - anodenascimento

# resposta de dados
print('-=' * 30)
for i, c in dados.items():
    print(f'{i} tem o valor {c}')
