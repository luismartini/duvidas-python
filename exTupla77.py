'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).

Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
palavras = (
    'Luís',
    'amigo',
    'Adele',
    'Jesus',
    'Deus',
    'Leitor',
    'Jonice',
    'Manoella',
)
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiouáéíó':
            print(letra, end=' ')