'''
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da terceira coluna;
c) O maior valor da segunda linha.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = maiorM = scol = 0

#Alimentação
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-' * 30)
#mostrar
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
#Soma da coluna
for l in range(0, 3):
    scol += matriz[l][2]

#Maior elemento da 2a linha
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

#Maior elemento da matriz
for l in range(3):
    for c in range(3):
        if matriz[l][c] == 0:
            maiorM = matriz[l][c]
        elif matriz[l][c] > maiorM:
            maiorM = matriz[l][c]

print('-' * 30)
print(f'A soma dos pares é: {spar}')
print(f'A soma dos valores da 3a coluna é: {scol}')
print(f'O maior valor da 2a linha é: {maior}')
print(f'O maior valor da matriz é {maiorM}')
