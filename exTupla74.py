'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e tam,bém indique o menor e o maior valor que estão na tupla.
'''
from random import randint

números = (randint(0,5), randint(0,5), randint(0,5), randint(0,5), randint(0,5))
print('Os valores sorteados foram: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO menor valor sorteado foi {min(números)}')
print(f'O maior valor sorteado foi {max(números)}')