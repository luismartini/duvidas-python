'''
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o valor 3
c) quais foram os números pares
'''

núm = (int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(input('Digite outro número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}.')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O número 3 apareceu na {núm.index(3)} posição ')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in núm: # varre a tupla
    if n % 2 == 0:
        print(f'{n}', end= ' ')