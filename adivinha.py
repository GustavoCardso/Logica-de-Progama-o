from random import randint
numeroUsurario = int(input('Digite um numero de 1 a 10: '))
numeroPc =  randint(0,10)
tentativas = 1

while numeroUsurario != numeroPc:
    if numeroUsurario < numeroPc:
        print('Mais... tente novamente!')
    elif numeroUsurario> numeroPc:
        print('Menos... tente novamente!')
    numeroUsurario = int(input('Você errou, digite novamente: '))
    tentativas += 1
print(f'Após {tentativas} tentativas você acertou!, o numero sorteado foi o {numeroPc}')