'''
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)
'''
quantidade = soma = 0
while True:
    n = int(input('Valor: '))
    if n == 999:
        break
    soma += n
    quantidade += 1
print(f'Foram digitados {quantidade}')
print(f'A soma foi {soma}')