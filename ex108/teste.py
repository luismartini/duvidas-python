import moeda

p = float(input('Qual o preço: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O preço aumentado em 13%, é {moeda.moeda(moeda.aumentar(p, 13))}')
print(f'O preço diminuído em 10% é {moeda.moeda(moeda.diminuir(p, 10))}')