def aumentar(preço=0, taxa=0, is_formatted=False):
    res = preço + (preço * taxa/100)
    return res if is_formatted else moeda(res) 

def diminuir(preço=0, taxa=0, is_formatted=False):
    res = preço - (preço * taxa/100)
    return res if is_formatted else moeda(res)

def dobro(preço=0, is_formatted=False):
    res = preço * 2
    return res if is_formatted else moeda(res)


def metade(preço=0, is_formatted=False):
    res = preço / 2
    return res if is_formatted else moeda(res)


def moeda(preço=0, moeda='R$', is_formatted=False):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'O dobro do preço:\t{dobro(preço)}')
    print(f'A metade do preço é:\t{metade(preço)}')
    print(f'{taxaa}% de aumento:\t\t{aumentar(preço, taxaa)}')
    print(f'{taxar}% de reducação:\t{diminuir(preço, taxar)}')
    print('-' * 30)
    