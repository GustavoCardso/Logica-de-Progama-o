valorCasa = float(input('Digite o valor da casa que você deseja comprar: '))
anos = float(input('Em quantos anos você deseja pagar: ')) * 12
salario = float(input('Informe o seu salário: '))
valorNecessario = (salario * 30) / 100


if valorNecessario >= valorCasa / anos:
    print(f'Você está apto a comprar este imovel, a parcela ira ficar no valor de R${valorCasa / anos:.2f}')
elif valorNecessario < valorCasa / anos:
    print('Não pode comprar tente algo que se encaixe no seu salario')
else:
    print('Você errou em alguma informação')