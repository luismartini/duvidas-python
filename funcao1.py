def soma(a, b):
    print(f'A soma entre {a} e {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    
    
#programa Principal
    #parâmetro
soma(8, 9)
soma(2, 1)
#soma(4)  #vai dar erro
soma(a=4, b=5)
soma(b=4, a=5)
soma(5, 3, *2)
