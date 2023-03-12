n = str(input('Digite o nome da cidade: ')).strip().lower()

d = n.split()[0]

print(f'A cidade começa com santo? \n{"santo" in d}')
