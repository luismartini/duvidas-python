'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol. Na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabela;
c) Uma lista com os times em ordem alfabética;
d) Em que posição na tabela está o time da Chapecoense
'''

times = ('Atlético', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América', 'Atlético-GO', 'Chapecoense')

print('x'*30)
print(f'Lista de times: {times}')
print('x'*30)
print(f'Os cinco primeiros times são: {times[0:5]}')
print('x'*30)
print(f'Os 4 últimos times são {times[-4:]}')
print('x'*30)
print(f"O Chapecoense está na posição {times.index('Chapecoense')+1} posição")
print('x'*30)
print(f'Em ordem alfabética é {sorted(times)}')