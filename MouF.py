n = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]

while n not in 'MmFf':
    n = str(input('Digite a opção selecionada [M/F]: ')).strip().upper()[0]
print(f'O sexo {n} foi registrado!')