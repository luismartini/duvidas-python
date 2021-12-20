'''
Prática de laços
'''
# valores = list()
# valores.append(5)
# valores.append(4)
# valores.append(9)

# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# print(valores)

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor{v}')

a = [2 ,3 ,4 ,5, 7]
b = a[:]  #cópia profunda
b[2] = 8  #shallow copy
print(f'Lista A: {a}')
print(f'Lista B: {b}')