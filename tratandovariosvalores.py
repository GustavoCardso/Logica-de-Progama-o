
soma = 0
qtd = 0


while True:
    n= int(input('Digite um numero [999 para parar] '))
    if n == 999:
        break
    soma += n
    qtd += 1
   
print(f'Você digitou {qtd} numeros e a soma total foi {soma}')