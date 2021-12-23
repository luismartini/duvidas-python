time = list()
jogador = dict()
partidas = list()
média = 0
cod = 0
while True:
    jogador.clear()
    jogador['nome'] = input('Nome: ')
    total = int(input(f'Partidas jogadas pelo {jogador["nome"]}: '))
    jogador['cod'] = cod
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
#Mostrar Tabela com o status de todos os jogadores
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
#Outra forma
# print(f"{'cod':^5} {'nome':^10} {'gols':<25} {'total':<25}")
# for jogador in time:
#     print(f"{jogador['cod']} {jogador['nome']} {jogador['gols']}")

print('-' * 30)
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
            print(f'No jogo {i} fez {g} gols')
    print('-' * 30)
