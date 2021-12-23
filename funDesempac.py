def soma(*valores):
    s = 0
    for núm in valores:
        s += núm
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)
soma(1)
soma(0)