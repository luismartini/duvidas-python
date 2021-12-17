'''
Maior e menor valor usando lógica
'''
resp = 'S'
qtd = maior = menor = 0

while resp in 'Ss':
    núm = int(input('Digite um número: '))
    qtd += 1
    if qtd == 1:
        maior = menor = núm
    if núm > maior:
        maior = núm
    if núm < menor:
        menor = núm
        
    resp = input('Quer continuar? [S/N] ').upper().strip()
print(f'Você digitou {qtd} números')
print(f'O maior valor digitado foi {maior} e o menor {menor}')