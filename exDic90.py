'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
aluno = dict()
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f"Média de {aluno['Nome']}: "))

if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Média'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print(aluno)

for k, v in aluno.items():
    print(f'- {k}: {v}')

