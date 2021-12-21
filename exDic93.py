'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
jogador = dict()
partidas = list()
média = 0
jogador['nome'] = input('Nome: ')
total = int(input(f'Partidas jogadas pelo {jogador["nome"]}: '))
for c in range(0, total):
    partidas.append(int(input(f'Gols na partida {c + 1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
# Primeira forma
print('=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 30)

#Segunda
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foram um total de {jogador["total"]} gols')
média = jogador['total'] / 2
print(f'A média de gols foi {média:.0f}')