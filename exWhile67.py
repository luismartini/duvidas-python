'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    valor = int(input(f'Valor: '))
    if valor < 0:
        break
    print('=' * 30)
    print(f'Tabuada do {valor}')
    for v in range(0, 11):
        print(f'{valor} x {v} = {valor * v}')
    print('=' * 30)

print('Acabou')