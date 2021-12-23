'''
CÓDIGO MAIS BEM TRABALHADO
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
jogador = dict()
gols = list()

#nome e partidas:
jogador['nome'] = input('Nome: ')
jogador['partidas'] = int(input(f"Partidas de {jogador['nome']}: "))

#Gols por partida:
for g in range(0, jogador['partidas']):
    gols.append(int(input(f'Gols partida {g+1}: ')))
jogador['gols'] = gols[:]
jogador['total_gols'] = sum(gols)

print(f"O jogador {jogador['nome']} apresentou-se em {jogador['partidas']} partidas e fez um total de {jogador['total_gols']} gols")

#Minucinado as partidas
for k, v in enumerate(jogador['gols']):
    print(f"Na partida {k+1}, o jogador {jogador['nome']} fez {v} gols")

