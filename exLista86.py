'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores pelo teclado.

3 linhas e 3 colunas

No fina, mostre a matriz na tela, com a formatação correta.
'''
matriz = list()
linha = list()
coluna = list()

for l in range(3):
    linha.append(matriz)
    for c in range(3):
        coluna.append(matriz)
        matriz.append(int(input((f'Digite um valor para [{l}, {c}]: '))))


