time = list()
jogador = dict()
partidas = list()
média = 0
while True:
    jogador.clear()
    jogador['nome'] = input('Nome: ')
    total = int(input(f'Partidas jogadas pelo {jogador["nome"]}: '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Conituar [S/N]? ').upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N!')
    if resp == 'N':
        break
#Mostrar Tabela
print('=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
#Interagir com dados
while True:
    busca = int(input('Dados de qual jogador: '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Não existe o código')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
    print('-' * 30)
