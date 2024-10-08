tot = 0
maisdemil = 0
menor = 0
soma = 0
cont = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Preço: '))
    res = ' '
    cont += 1
    soma += preco
    if preco >= 1000:
        maisdemil += 1         
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    while res not in 'SN':
        res = str(input('Quer continuar?[S/N]')).strip().upper()[0]   
    if res == 'N':
        break
print(f'O valor total das compras foi {soma}', end= ' ')
print(f'Temos {maisdemil} produtos custando mais de mil reais', end= ' ')
print(f'O produto mais barato foi {produto}')