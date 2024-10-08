anoNascimento = int(input('Digite o ano que você nasceu: '))
anoAtual = 2024
idade = anoAtual - anoNascimento


if anoAtual - anoNascimento  < 18:
    print(f'Você ainda vai se alistar, faltam {18 - idade} anos')
elif anoAtual - anoNascimento > 18:
    print(f'Você já deveria ter se alistado fazem {idade- 18} anos!')
else:
    print('Você se alsita esse ano!')