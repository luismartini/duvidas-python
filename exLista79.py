números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        print(f'O valor {n} foi adcionado com sucesso')
    else:
        print('Valor duplicado! Não vou adcionar...')
    
    r = str(input('Quer continuar? [S/N]'))[0]
    if r in 'Nn':
        break
números.sort()
print(f'Você digitou os valores {números}')