n = int(input('Digite um valor: '))

u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'A unnidade é {u}')
print(f'A dezena é {d}')
print(f'A centena é {c}')
print(f'A milhar é {m}')
