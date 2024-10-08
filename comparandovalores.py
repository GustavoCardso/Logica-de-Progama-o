n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))

if n1 > n2:
    print(f'O numero 1 {n1} é maior que o numero 2 {n2}')
elif n2 > n1:
    print(f'O numero 2 {n2} é maior que o numero 1 {n1}')
else:
    print('Os numeros são iguais')