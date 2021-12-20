'''
Faça um programa que leia o nome e o peso de várias pesoas, guardado tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessas mais pesadas;
c) Uma listagem com as pessoas mais leves
'''
pessoas = list()
peso = list()
dados = list()
pesada = list()
leve = list()
pdig = ppesada = pleve = 0

while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    peso.append(dados[:])
    dados.clear()

    resp = input('Continuar [S/N]: ')
    if resp in 'Nn':
        break
print(pessoas)
print(pdig)
print(pesada)
print(leve)