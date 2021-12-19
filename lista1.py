'''
Listas (Parte 1)
São mutáveis
'''
'''
lanches = ['Hamburger', 'Suco', 'Pizza', 'Pudim']
lanches[0] = 'Churrasco'
print(lanches)
'''
'''
Adicionar
lanches = ['Hamburger', 'Suco', 'Pizza', 'Pudim']
#lanches.append('Caramelo')
print(lanches)
lanches.insert(0, 'Sushi')
print(lanches)
#print(lanches.index('Pudim'))
print(lanches.append('Hot Dog'))  #No final
'''
'''
apagar elementos
del
pop() - último elemento
remove() - indica o valor
'''
'''
lanches = ['Hamburger', 'Suco', 'Pizza', 'Pudim']
#del lanches[3]
#lanches.pop()
if 'amigos' in lanches:
    lanches.remove('amigos')
print(lanches)
'''
'''
Criar listas a partir de for
valores = list(range(4, 11))
print(valores)
'''
'''
valores = [4,2,5,3,0,9]
print(valores)
valores.sort(reverse=True)
print(valores)
print(sorted(valores))
print(len(valores))
'''