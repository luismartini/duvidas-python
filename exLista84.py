'''
Faça um programa que leia o nome e o peso de várias pesoas, guardado tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves
'''
pessoal = list()
dados = list()
maior = menor = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoal) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoal.append(dados[:])
    dados.clear()

    resp = input('Continuar [S/N]: ')
    if resp in 'Nn':
        break
print('-' * 30)
#print(pessoal)
print(f'Ao todo foram cadastradas {len(pessoal)} pessoas')      #uso de len no lugar de contador.
print(f'A pessoa mais pesada é {maior}kg. Peso de ', end='')
for p in pessoal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'A pessoa mais leve é {menor}kg. Peso de ', end='')
for p in pessoal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()