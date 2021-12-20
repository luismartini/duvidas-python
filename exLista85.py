'''
Crie um programa em que o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha sepados os valores pares e ímpares. 
No final mostre os valores pares e ímpares em ordem crescente.
'''
número = list()
#número = [[], []]
pares = list()
ímpares = list()
for n in range(0, 7):
    número = int(input(f'Digite o {n+1} números: '))
    if número % 2 == 0:
        pares.append(número)
    else:
        ímpares.append(número)
print(f'Os números pares são {sorted(pares)}')
print(f'Os números ímpares foram {sorted(ímpares)}')

'''
núm = [[], []]
valor = 0
for c in range(0, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-' * 30)
print(f'Todos os valores: {núm}')
print(f'Os valores pares {núm[0]}')
print(f'Os valores ímpares {núm[1]}')
'''