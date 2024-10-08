valor = float(input('Digite o valor da compra: '))
metodo = str(input('Digite o metodo de pagamento. 1-Dinheiro, 2-Cheque, 3-Cartão avista, 4-Cartão em até 2x, 5- Cartão 3x. ')).strip()

if metodo == '1' or metodo == '2':
    print(f'Você recebeu 10% de desconto, o valor da compra ficou de R${valor - (valor * 10)/ 100 }')
elif metodo == '3':
    print(f'Você recebeu 5% de desconto, o valor da compra ficpu de R${valor - (valor * 5) / 100}')
elif metodo == '4':
    print(f'O valor da compra ficou em {valor}')
elif metodo == '5':
    print(f'Com os juros, o valor da sua compra ficou em R${valor + (valor * 25) / 100}')
else:
    print('Você não selecionou nenhumas opções!')