from datetime import date 
atual = date.today().year 
totMaior = 0
totMenor = 0

for pess in range(1,8):
    nasc =  int(input(f'Em que ano a {pess}° nasceu?'))
    idade = atual - nasc
    if idade >= 21:
        totMaior += 1
    else:
        totMenor += 1
print(f'Ao todo tivemos {totMaior} pessoas maiores de idade!')
print(f'Ao todo tivemos {totMenor} pessoas menores de idade!')