'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
valor = int(input('Valor a ser sacado: R$'))
total = valor 
cédula = 50
totcéd = 0
while True:
    if total >= cédula:
        total -= cédula
        totcéd += 1
    else:
        print(f'Total de {totcéd} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totcéd = 0
        if total == 0:
            break