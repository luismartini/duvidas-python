'''
While (Flag)
'''
# cont = 1
# while cont <= 10:
#     print(cont, '-> ', end='')
#     cont += 1
# print('Acabou')


# while True: executa para sempre
# cont = 1
# while True:
#     print(cont, '-> ', end='')
#     cont += 1
# print('Acabou!')

n = soma = 0
#flag = 999
# break tira a flag da contagem
while n != 999:
    n = int(input('Número: '))
    if n == 999:
        break
    soma += n
print(f'A soma vale {soma}')