n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
opcao =  0
um = n1 + n2
multiplicar = n1 * n2


while opcao != 5:
    opcao = int(input('Digite o que você deseja fazer. Somar[1], Mulitplicar[2], Maior[3], Novo numero[4], Sair[5].'))
    
    if opcao == 1:
        print(f'A Soma dos dois numeros são {n1 + n2}')
    if opcao == 2:
        print(f'A mutiplicação dos dois numeros são: {n1 * n2}')
    if opcao == 3:
        if n1 > n2:
            print(f'O 1° numero ({n1}) é maior que o 2° numero({n2})')
        elif n1 < n2:
            print(f'O 2° numero({n2}) é maior que o 1° numero ({n1})')
        elif n1 == n2:
            print('Os numeros são iguais!')
    if opcao == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
    if opcao == 5:
        print('Progama encerrando...')
    elif opcao == 0 or opcao > 5:
        print('Opção invalida tente novamente!')
    
print('Você saiu do progama')   

