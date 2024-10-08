
print('Cadastre uma pessoa')
maisdzt = totH = mulhermaisvnt = 0


while True:
    idade = int(input('Idade:'))
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
            maisdzt += 1
    elif sexo == 'M':
            totH += 1
    elif sexo == 'F' and idade < 20:
            mulhermaisvnt += 1
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if conti == 'N':
        break
print(f'Total de pessoas cadastradas com mais de 18 anos, {maisdzt} pessoas', end=' ')
print(f'Ao todo temos {totH} homens cadastrados', end= ' ')
print(f'Temos {mulhermaisvnt} mulheres com menos de 20 anos')
