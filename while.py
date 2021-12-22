'''
Uso de while
'''
# for c in range(1, 10):
#     print(c)
# print('Fim')

# c = 1
# while c < 10:
#     print(c)
#     c += 1
# print('Fim')

'''
while - quando não sei o limite
'''
# n = int(input('Número: '))
# c = 0
# while c < n:
#     print(c)
#     c += 1

#  Com soma
# soma = 0
# for c in range(0, 3):
#     n = int(input(f'Um {c} valor: '))
#     soma += n
# print(soma)
# print('FIM')

# Com resposta
# r = 'S'
# while r == 'S':
#     n = int(input('Valor: [0 para] '))
#     r = input('Quer continuar [S/N]? ').upper()
# print('Fim')

# r = 'S'
# while r == 'S':
#     cont = 0
#     n = int(input('Valor: [0 para] '))
#     cont += 1
#     r = input('Quer continuar [S/N]? ').upper()
# print(cont)
# print('Fim')

# Pares e Ímpares
# Para não analisar o flag
n = 1
par = ímpar = 0
while n != 0:
    n = int(input('Valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            ímpar += 1
print(f'Você digitou {par} pares e {ímpar} ímpares')
print('ACABOU!')
