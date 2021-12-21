estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = input('Unidade federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())  #copy
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
