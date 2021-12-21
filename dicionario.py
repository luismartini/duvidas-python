'''
Aula sobre Dicionário - estrutura de dados compostas
tuplas - ()
listas - []
# índices numéricos
dicionários - {}
# índices literais
'''
print('-' * 50, f'\nEstrutura Composta: Dicionários\n', '-' * 50,)
# dados = dict()
# dados = {'nome': 'Pedro', 'idade': 25}
#         #valor  #identificador
# dados['sexo'] = 'Masculino'
# #print(dados['nome'])  #Pedro
# #print(dados['idade'])  #25
# print(dados)  #{'nome': 'Pedro', 'idade': 25, 'sexo': 'Masculino'}
# del dados['idade']
# print(dados)  #{'nome': 'Pedro', 'sexo': 'Masculino'}
'''
Não trabalha com índices numéricos, mas com literais
'''
# chaves/keys valor
filme = {
    'título': 'StarWars',
    'ano': 1977,
    'diretor': 'George Lucas',
}
#Valores
print(filme.values())  #dict_values(['StarWars', 1977, 'George Lucas'])
#Chaves
print(filme.keys())  #dict_keys(['título', 'ano', 'diretor'])
# Todos os ítens
print(filme.items())  #dict_items([('título', 'StarWars'), ('ano', 1977), ('diretor', 'George Lucas')])

for k, v in filme.items():
    print(f'O {k} é {v}')

for v in filme.values():
    print(v)