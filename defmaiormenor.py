while True:
    def maior(x, y, z):
        Maior = x
            
        if y > Maior:
            Maior = y
        if z > Maior:
            Maior = z
        return Maior

    def menor (x, y, z):
        Menor = x
            
        if y < Menor:
            Menor = y
        if z < Menor:
            Menor = z
        return Menor
    def menu():
        x = int(input('Primeiro número: '))
        y = int(input('Segundo número: '))
        z = int(input('Terceiro Número: '))
        print('Maior: ', maior(x,y,z))
        print('Menor: ', menor(x,y,z))
        resp = 'S'
        if resp == 'S':
            resp = input('Quer continuar [S/N]').upper().strip()
        if resp == 'N':
            print('Acabou a brincadeira!')

    while True:
        menu()