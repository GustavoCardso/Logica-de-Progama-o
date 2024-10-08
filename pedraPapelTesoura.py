import random
print('Vamos jogar Jokenpô!')
jogador = str(input('Digite o que você quer! Pedra, papel ou tesoura: '))
pc = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(pc)

print(f'Você selecionou {jogador} e o computador {computador}, por tanto...')
if computador == 'Pedra' and jogador == 'Tesoura':
    print('O computador ganhou!')
elif computador == 'Tesoura' and jogador == 'Papel':
    print('O computador ganhou!')
elif computador == 'Papel' and jogador == 'Pedra':
    print('O computador venceu!')
elif computador == jogador:
    print('Vocês escolheram a mesma coisa kk')
else:
    print('Você venceu!')