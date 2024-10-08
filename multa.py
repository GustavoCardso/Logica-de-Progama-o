velocidade = int(input('Digite a velocidade do carro: '))
valor = velocidade[:0] * 7


if velocidade > 80:
    print(f'Você levou uma multa o valor será de R${valor}')
else:
    print('Você não levou uma multa')