'''
Crie um programa que tenha a função leiaInt(), 
que vai funcionar de forma semelhante à função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico. 
Ex: n = leiaInt(‘Digite um n: ‘)
'''
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite apenas números inteiros\033[m')
        if ok:
            break
    return valor

#PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')