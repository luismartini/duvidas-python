'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep
def maior(*núm):  #como não sei quantos parâmetros, usamos o *núm
    cont = maior = 0
    print('-' * 30)
    print('\nAnalisando os valores passados...')
    for valor in núm:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.2)
        
        if cont == 0:
            maior = valor 
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')

#PROGRAMA PRINCIPAL
maior(2, 9, 7, 3, 1, 20)
maior(4, 6, 2, 1)
maior(2, 1, 0)
maior(6)
maior()