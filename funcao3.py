def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos +=1


valores = [6, 3, 9, 0, 2]
dobra(valores)
print(valores)

#passagem de parâmetro por referência