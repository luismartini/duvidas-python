'''
Função (Parte 2)
1. help() - ok
2. Docstrings()
3. Argumentos opcionais
4. Escopo de variávies
5. retorno de resultados
'''

'''
help(valor)
'''

'''
DocStrings -> fazer o manual completo
    """[summary]
    """
'''

'''
def contador(i, f, p):
    """
    [Contador]
    Args:
        i ([i]): [início]
        f ([f): [Fim]
        p ([p]): [passos a serem pulados]
        return: sem retorno
        Função criada por Luís Martini
    """
    c = 0
    while c <= f:
        print(f'{c}', end='...')
        c+=p
    print('Fim')
    
help(contador)

#contador(0, 10, 2)
'''

'''
Parâmetros opcionais
somar(a, b, c=0), c=0 é parâmetro opcional

def somar(a=0, b=0, c=0):
    """
    [somar]

    Args:
        a ([a]): [Primeiro valor, pode ser opcional =0]
        b ([b]): [Segundo valor, pode ser opcional =0]
        c ([c]): [Terceiro valor, pode ser opcional =0]
    """
    s = a + b + c
    print(f'O resultado é {s}')


help(somar)
somar(3, 2, 5)
somar(8, 4)
somar(8)
somar()
somar(a=5, c=2)
'''

'''
Escopo de variáveis
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

n = 2
#Programa Principal
teste()
print(f'No programa principal n vale {n}')
'''
'''
def teste(b):

    b += 4  #escopo local
    c = 2  #escola local
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a=5  #escopo global
teste(a)

def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
função()
print(f'N1 fora vale {n1}')

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
'''

'''
Retorno de valor
return
'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    #print(f'A soma vale {s}')
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')