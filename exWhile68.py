from random import randint
v = 0
while True:
    jogador = int(input('Valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou ímpar? ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes!')