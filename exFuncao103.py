'''
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou.
O programa deverá mostrar a ficha d jogador, mesmo que algum dado não tenha sido 
informado.
'''
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol/gols na partida!')


# PROGRAMA PRINCIPAL
n = input('Nome: ')
g = input('Gol: ')  #str deixa ficar vazio

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)  #nome vazio, passo apenas os gols
else:
    ficha(n, g)