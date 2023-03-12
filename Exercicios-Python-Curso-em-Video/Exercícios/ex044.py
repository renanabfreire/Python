valorinicial = float(input('Digite o preço normal do produto: R$'))

print('\nOpções de pagamento:'
      '\n\033[7m(1)\033[0mÀ vista no dinheiro ou cheque[10% de desconto]'
      '\n\033[7m(2)\033[0mÀ vista no cartão[10% de desconto]'
      '\n\033[7m(3)\033[0m2x no cartão'
      '\n\033[7m(4)\033[0m3 ou mais vezes no cartão[20% de juros]')

formadepagamento = int(input('Sua opção: '))

if formadepagamento == 1 or formadepagamento == 2 or formadepagamento == 3 or formadepagamento == 4:
    if formadepagamento == 1:
        desconto = 10 * valorinicial / 100
        valornovo = valorinicial - desconto
        print('\nVocê deverá pagar R${:.2f} com R${:.2f} de desconto.'.format(valornovo, desconto))
    elif formadepagamento == 2:
        desconto = 5 * valorinicial / 100
        valornovo = valorinicial - desconto
        print('\nVocê deverá pagar R${:.2f} com R${:.2f} de desconto.'.format(valornovo, desconto))
    elif formadepagamento == 3:
        print('\nVocê deverá pagar R${}.'.format(valorinicial))
    else:
        juros = 20 * valorinicial / 100
        valornovo = valorinicial + juros
        print('\nVocê deverá pagar R${:.2f} com um juros de R${:.2f}.'.format(valornovo, juros))

else:
    print('\nEssa opção não está disponível!')
