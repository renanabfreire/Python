print(15 * '-=')
tbr = ('Palmeiras', 'Corinthians', 'Internacional', 'Atlético-MG', 'Fluminense', 'Athletico', 'São Paulo', 'Santos',
       'Flamengo', 'Botafogo', 'RB Bragantino', 'Goiás', 'Cuiabá', 'Coritiba', 'América-MG', 'Avaí', 'Ceará',
       'Atlético-GO', 'Juventude', 'Fortaleza')
print(f'Lista de times do Brasileirão: {tbr}')
print(15 * '-=')
print(f'Os 5 primeiros são {tbr[:5]}')
print(15 * '-=')
print(f'Os 4 últimos são {tbr[-4:]}')
print(15 * '-=')
print(f'Times em ordem alfabética: {sorted(tbr)}')
print(15 * '-=')
print(f'O Flamengo está na {tbr.index("Flamengo") + 1}ª posição.')
