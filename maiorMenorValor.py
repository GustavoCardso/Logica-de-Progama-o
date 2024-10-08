
qtd = 0 
media = 0
soma = 0
r = 'S'
maisVelho = 0
maior = 0
menor = 0
while r in 'Ss':
    n = int(input('Digite um numero: '))   
    qtd += 1
    media += 1
    soma += n
    r =  str(input(('Quer continuar[S/N]: '))).strip().upper()[0]
    if qtd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'Você digitou {qtd} numeros e a media foi de {soma / qtd}', end= '')
print(f'O maior valor fpo {maior} e o menor foi {menor}')