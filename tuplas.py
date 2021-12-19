'''
Tuplas - Variáveis Compostas (lista[], dicionário{})
Uso de (...)
'''

'''
Base de fundamentos
Variáveis compostas são múltiplas
Manipular a tupla...
'''

'''
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lanche[2])  #pizza
print(lanche[0:2])  #('hamburger', 'suco')
print(lanche[1:])  #('suco', 'pizza', 'pudim')
print(lanche[-1])  #pudim
print(len(lanche))  #4
'''

'''
for item in lanche:
    print(item)
'''

'''
Manipulação - As tuplas são imutáveis
'tuple' object does not support item assignment
'''

'''
Parte Prática da Aula
sorted() - colocar em lista/em ordem
'''

'''
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
#print(lanche[:]) kkkk
#print(lanche[:2:])  #('Hamburger', 'Suco')
#print(len(lanche))
print(sorted(lanche))
# for pos, comida in enumerate(lanche):
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {comida} na posiçao {pos}')
# for comida in lanche:
#     print(f'Eu vou comer {cont}')
# print('Comi para caramba!!')
'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
#print(a)
#print(b)
#print(c)
#print(len(c))
#print(c.count(4))
#print(c.index(5, 1))  #primeira ocorrência
#print(sorted(c))
#del(c[0])  #pode apagar a tupla inteira
print(a)
print(b)
print(c)