n1 = float(input('Digite a nota do aluno: '))
n2 = float(input('Digite a nota do aluno: '))
media = (n1 + n2) / 2


if media < 5.0:
    print(f'Aluno reprovado, a média dele foi de {media:.2f}')
elif media <= 6.9:
    print(f'Aluno em recuperação, a média dele foi de {media:.2f}')
else:
    print(f'Aluno aprovado, sua média foi de {media:.2f}')