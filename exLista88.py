'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep

lista = list()
jogos = list()
print('-' * 30)
print('Joga na Mega Sena')
print('-' * 30)
quantidade = int(input('Quantos jogos você quer que eu dê palpite? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        núm = randint(0, 60)
        if núm not in lista:
            lista.append(núm)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-' * 3, f'SORTEANDO {quantidade} JOGOS', '-' * 3)
sleep(0.5)
for jogo, palpite in enumerate(jogos):
    print(f'jogo {jogo+1}: {palpite}')
    sleep(1)
print('-' * 5, f'BOA SORTE', '-' * 5)
