produtos = ('Lapís', 1, 'Caneta', 3, 'Borracha', 2.50, 'Caderno', 10, 'Mochila', 80, 'Penal', 20)
print(('-' * 30))
print(          'LISTAGEM DE PREÇO')
print(('-' * 30))

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end= '')
    else:
        print(f'R${produtos[pos]:>7.2f}')