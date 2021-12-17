'''
Crie uma programa que tenha uma tupla totalmente preenchida com uma contagem por extensão de zero até vinte

Seu programa dever ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
'''
números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        n = int(input('Digite um número entre [0 e 20]: '))
        if 0 <= n <= 20:  #menor igual
            break
        print('Tente novamente. ', end='')
    print(f'O número digitado foi {números[n]}')
    resp = input('Deseja continuar? [S/N]: ').upper().strip()
    if resp == 'N':
        break