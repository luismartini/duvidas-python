'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def área(larg, comp):
    a = l * c
    print(f'A área do retángulo é: {a}m2')
    
def mensagem(msg):
    print(msg)

def lin():
    print('-' * len('Controle de terrenos alien'))


#PROGRAMA PRINCIPAL
# msg = input('Mensagem: ')
# mensagem(msg)
mensagem(msg='Controle de Terreno alien')
lin()
l = int(input('Largura: '))
c = int(input('Comprimento: '))
área(l, c)