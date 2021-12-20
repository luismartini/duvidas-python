'''
Crie um programa em que o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha sepados os valores pares e ímpares. 
No final mostre os valores pares e ímpares em ordem crescente.
'''
número = list()
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