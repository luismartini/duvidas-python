'''
Faça um programa que tenha uma função notas() 
que pode receber várias notas de alunos e 
vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma 
– A situação (opcional)
'''
def nota(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    
    return r

#PROGRAMA PRINCIPAL
resp = nota(5.5, 7.5, 6.5, 9.0, sit=True)
print(resp)