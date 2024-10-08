n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
doisLados = n1 + n2

if doisLados > n3 and n1 == n2 ==n3:
    print('é possivel formar um triangulo equilatero')
elif doisLados > n3 and n2 == n1:
    print('Print é possivel formar um triangulo issoseles')
elif doisLados > n3 and n1 != n2 != n3:
    print('É possivel formal um triangulo escaleno')
else:
    print('Não é possivel formar um triangulo')