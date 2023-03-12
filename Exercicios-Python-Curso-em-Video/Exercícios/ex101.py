def voto(nasc):  # função para saber opção do voto
    # Importando bibliotecas
    from datetime import date

    idade = date.today().year - nasc  # Obtendo idade

    # Avaliando situação
    if 16 <= idade < 18 or idade > 65:
        sit = 'VOTO OPCIONAL'
    elif idade >= 18:
        sit = 'VOTO OBRIGATÓRIO'
    else:
        sit = 'NÃO VOTA'

    print(f'Com {idade} anos: {sit}.')


# Códio principal
print(30 * '-')
n = int(input('Em que ano você nasceu? '))  # Obtendo data
voto(n)  # Devolvendo situação
