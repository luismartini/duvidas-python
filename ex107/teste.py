from uteis import números

p = float(input('Qual o preço: '))
print(f'A metade de {p} é {números.metade(p)}')
print(f'O dobro de {p} é {números.dobro(p)}')
print(f'O preço aumentado em 13%, é {números.aumentar(p, 26)}')
print(f'O preço diminuído em 10% é {números.diminuir(p, 10)}')