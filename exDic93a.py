'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
jogador = dict()
partidas = list()
total = 0

#nome/partidas
jogador['nome'] = input('Nome do jogador: ')
total = int(input(f"Partidas disputadas por {jogador['nome']}: "))

#Gols a cada partida
for c in range(0, total):
    partidas.append(int(input(f'Quanto gols por partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

print(f"O jogador {jogador['nome']} jogou {jogador['total']} e fez {jogador['gols']} por partida")

for k, v in enumerate(jogador['gols']):
    print(f"Na partida {k + 1}, fez {v} gols")
print(f"Ao todo, o {jogador['nome']} fez {sum(partidas)} gols")
#print(f"Ao todo, {jogador['nome']} fez {jogador['total']} gols")
