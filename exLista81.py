'''
Crie um programa que vai ler vários números e colocar uma lista.

Depois disso, mostre:

a) Quantos números foram digitados;

b) A lista de valores ordenados de forma decrescente

c) Se o valor 5 foi digitado e está ou não na lista
'''
valor = list()
while True:
    valor.append(int(input('Digite um valor: ')))
    
    r = input('Deseja continuar [S/N]: ')
    if r in 'Nn':
        break
print(f'Os valores lidos foram {valor}')