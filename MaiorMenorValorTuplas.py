import random
#Gerando 5 números aleatórios entre 10 e 30
lista_aleatoria = random.sample(range(10, 30), 5)
print(lista_aleatoria) 
print(f'O maior numero da lista é {max(lista_aleatoria)}')
print(f'O menor numero da lista é {min(lista_aleatoria)}')