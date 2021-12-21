'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores pelo teclado.

3 linhas e 3 colunas

No fina, mostre a matriz na tela, com a formatação correta.
'''

'''

for l in range(3):
    linha.append(matriz)
    for c in range(3):
        coluna.append(matriz)
        matriz.append(int(input((f'Digite um valor para [{l}, {c}]: '))))
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))

print('-' * 30)

for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
#print(matriz)
