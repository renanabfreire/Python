def leiadinheiro(num):
    while True:
        n = str(input(num))
        if ',' in n:
            temp = (n).replace(",", ".")
        else:
            temp = n

        try:
            n = float(temp)
            return n
        except ValueError:
            print(f'ERRO: "{n}" é um preço inválido.')
