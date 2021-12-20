'''
Crie um programa onde o usuário digite uma expressão qualquer que use parêntreses. Seu aplicativo deverá analisar se a expressão passada está com os parêntres abertos e fechados na ordem correta.
'''
expr = input('Digite a expressão: ')
pilha = list()
for símbolo in expr:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')
