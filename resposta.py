while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Idade: '))
    resp = input('Quer continuar [S/N]? ')
    if resp in 'Nn':
        print('Acabou!')

