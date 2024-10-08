anoNascimento = int(input('Digite o ano do seu nascimento: '))
idade = 2024 - anoNascimento

if idade < 9:
    print('Esse competidor é da categoria mirim')
elif idade <= 14:
    print('Esse competidor é da categoria juvenil')