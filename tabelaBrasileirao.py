"""Crie uma tabela do brasileirão, e mostre a posição doso 4 ultimos, dos 4 primeiro e a posição do cuiaba
    """
times = 'Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Bahia', 'Internacional', 'Cruzeiro', 'Vasco', 'Atletico-MG', 'Bragantino', 'Gremio', 'Juventude', 'Criciuma', 'Athletico-PR', 'Vitória', 'Fluminense', 'Corinthans', 'Cuiaba', 'Atletico-GO'
print(f'Os time dos Brasileirão são: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos são {times[16:20]}')
print('-=' * 15)
print(f'A posição do Cuiaba é {times.index("Botafogo") + 1}')
print('-=' * 15)
print(f'Os times em ordem alfabéticas: {sorted(times)}')
