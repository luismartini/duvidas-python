def aumentar(preço=0, taxa=0, is_formatted=False):
    res = preço + (preço * taxa/100)
    return res if is_formatted else res 

def diminuir(preço=0, taxa=0, is_formatted=False):
    res = preço - (preço * taxa/100)
    return res if is_formatted else res

def dobro(preço=0):
    return preço * 2


def metade(preço=0):
    return preço / 2


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

