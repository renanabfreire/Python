p = str(input('Digite o termo: ')).lower().split()
t = str(''.join(p))

d = ' '

n = len(t)

for c in range(0, n):
    if t[c] != t[n - 1]:
        d = ' não '

    n -= 1

print(f'O termo{d}é um palídromo!')
