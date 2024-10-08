from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O angulo de {angulo} tem o seno de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O angulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem a tangente de {tangente:.2f}')