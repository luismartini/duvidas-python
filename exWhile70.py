'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''
totGasto = prodmil = menor = maior = cont = 0
nomeBarato = ' '
nomeCaro = ' '
while True:
    produto = input('Produto: ')
    preço = float(input('Preço: R$ '))
    cont +=1
    #total de gastos
    totGasto += preço

    # Produtos mais caros
    if preço >= 1000:
        prodmil += 1
    
    #nome do produto mais barato
    
    if cont == 1:
        menor = preço
        nomeBarato = produto
    else:
        if preço < menor:
            menor = preço
            nomeBarato = produto
        if preço > maior:
            maior = preço
            nomeCaro = produto
    #resposta
    resp = ' '
    while resp not in 'SN':
        resp = input('Continuar [S/N]? ').upper()[0]
    if resp == 'N':
        break

print(f'O total de gastos foram R${totGasto}')
print(f'Produtos acima de R1000 são: R${prodmil}')
print(f'O nome mais caro é {nomeCaro}')
print(f'O nome do produto mais barato foi {nomeBarato} e custa R${menor}')