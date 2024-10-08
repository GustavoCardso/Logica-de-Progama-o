n1 = int(input(('Digite um numero: ')))
n2 = int(input(('Digite outro numero: ')))
n3 = int(input(('Digite mais um numero: ')))
n4 = int(input(('Digite o ultimo numero: ')))
valores = (n1, + n2, + n3 ,+ n4)
print(f'Você digitou os numeros {valores}')
print(f'O numero 9 apareceu {valores.count(9)} vezes')
if valores == 3:
    print(f'O primeiro numero 3 digitado foi na posição {valores.index(3) + 1}')
else:
    print('O valor 3 não foi digitado')
print(f'O valores pares são ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
