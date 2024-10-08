from datetime import date 
masculino = 'M'
feminino = 'F'
maiorIdadeHomem = 0
nomeVelho = ''
totalMulher20 = 0


for pess in range(1, 5):
    print(f'----- {pess}° Pessoa -----')
    nome = str(input(f'Digite o nome da {pess}° pessoa: '))
    sexo = str(input(f'Digite o sexo da {pess}° pessoa: '))
    idade = int(input(f'Digite a idade da {pess}° pessoa: '))
    anos = pess * idade
    if pess == 1 and  sexo in 'Mm':
        maiorIdadeHomem =  idade 
        nomeVelho =  nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher20 += 1
        
print(f'A média de idade das pessoas é de {anos/ 4}')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}')
print(f'Ao todo são {totalMulher20} mulheres com menos de 20 anos!')



