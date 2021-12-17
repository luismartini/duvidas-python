def maior(x, y, z):
    max = x
    
    if y > max:
        max = y
    if z > max:
        max = z
    return max
def menor (x, y, z):
    min = x
    if y < min:
        min = y
    if z < min:
        min = z
    return min
def menu():
    x = int(input('Primeiro número: '))
    y = int(input('Segundo número: '))
    z = int(input('Terceiro Número: '))
    
    print('Maior: ', maior(x,y,z))
    print('Menor: ', menor(x,y,z))

while True:
    menu()