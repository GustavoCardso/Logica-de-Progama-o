print("gerador de PA")
print("=-=" * 10)
p1 = int(input("primeiro termo:"))
r = int(input("razão:"))
termo = p1 
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->',end= '')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print("FIM")
print(f'ao todos foram mostrados {total} numero')