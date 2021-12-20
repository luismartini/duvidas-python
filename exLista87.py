'''
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da terceira coluna;
c) O maior valor da segunda linha.
'''
matriz = list()
linha = list()
coluna = list()

for l in range(3):
    linha.append(matriz)
    for c in range(3):
        coluna.append(matriz)
        matriz.append(int(input((f'Digite um valor para [{l}, {c}]: '))))