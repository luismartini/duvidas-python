'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
maior = menor = 0
listanum = []
for v in range(0, 5):
    listanum.append(int(input(f'Digite um número para a posição {v}: ')))
    
    if v == 0:
        maior = menor = listanum[v]
    else:
        if listanum[v] > maior:
            maior = listanum[v]
        if listanum[v] < menor:
            menor = listanum[v]

print('-' * 30)
print(f'Os valores digitados foram {listanum}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
        
print(f'\nO menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')


# print(f'O maior valor digita foi {max(valores)}')
# print(f'O menor valor digitado foi {min(valores)}')
