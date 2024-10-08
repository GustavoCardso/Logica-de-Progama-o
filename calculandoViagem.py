distancia = int(input('Qual a distancia da sua viagem?: '))
if distancia <= 200:
    print(f'A sua viagem custará {distancia * 0.50}')
else:
    print(f'A sua viagem custará {distancia * 0.45}')