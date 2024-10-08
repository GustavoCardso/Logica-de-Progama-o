import random

v = 0
while True:
    n = int(input('Digite um numero: '))
    pc = random.randint(0,10)
    total = n + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar[P/I]: ')).strip().upper()[0]
        print(f'Você jogou {n} e o computador {pc}, total de {total}. ', end='')
        print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
        if tipo == 'P':
            if total % 2 == 0:
                print('Você venceu!')
                v += 1
            else:
                print('Você perdeu!')
                break
        elif tipo == 'I':
            if total % 3 == 1:
                print('Você ganhou!')
                v += 1
            else:
                print('Você perdeu!')
                break
    print('Vamos jogar novamente...')

print(f'Gamer Over, você ganhou {v} vezes')