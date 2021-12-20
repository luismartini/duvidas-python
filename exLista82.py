'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados em ordem crescente.

Ao final, moster o conteúdo das três listas geradas.
'''
números = list()
pares = list()
ímpares = list()

while True:
    números.append(int(input('Digite um número: ')))

    resp = input('Continuar [S/N]? ')
    if resp in 'Nn':
        break
for i, v in enumerate(números):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)

print(f'A lista de números digitados foi {números}')
print(f'A lista de números pares foi {pares}')
print(f'A lista de ímpares foi {ímpares}')
'''
    if números % 2 == 0:
        pares.append(números)
    elif números % 2 == 1:
        ímpares.append(números)
'''    