'''
Parte prática
'''
pessoas = {
    'nome': 'Gustavo',
    'sexo': 'Masculino',
    'idade': 22
}
pessoas['nome'] = 'Luís'
pessoas['idade'] = 44

'''
keys(), values(), items()
'''

for v, k in pessoas.items():
    print(f'{v} = {k}')

#print(pessoas[0])  #KeyError: 0
# print(pessoas['nome'])  #Gustavo
# print(pessoas['idade'])  #22
# print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")  #O Gustavo tem 22 anos
# print(pessoas.keys())