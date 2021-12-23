'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
from random import randint

números = list()
def sorteia(lista):
    print('SORTEANDO 5 VALORES DA LISTA: \n', end='', flush=True)
    for cont in range(0, 5):
        n = randint(1, 10)
        números.append(n)
        print(f'{n}')
    print('PRONTO!')
    print(números)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

sorteia(números)
somaPar(números)
