'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário **em ordem**, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)
}

ranking = {}

#print(jogo)
print(f'Valor sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#print('-' * 30, f'\nRanking{v[0]}\n', '-' * 30)
print('-' * 30)
for i, v in enumerate(ranking):
    
    print(f'{i+1}o lugar: {v[0]} com {v[1]}')