aberto = fechado = 0
l = input('Digite sua expressão algébrica com parênteses: ')

for c in l:
    if c == '(':
        aberto += 1
    elif c == ')':
        fechado += 1

if aberto == fechado:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
