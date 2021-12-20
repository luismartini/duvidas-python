'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado!')
            
    r = input('Quer continuar [S/N]: ')
    if r in 'Nn':
        break
print('-' * 30)
números.sort()
print(f'Você digitou os valores {números}')