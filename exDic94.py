'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
cadastro = list()
pessoas = dict()
total = 0
soma = média = 0

while True:
    pessoas.clear()
    pessoas['nome'] = input('Nome: ')
    while True:
        pessoas['sexo'] = input('Sexo: ').upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Aceita-se apenas M ou F')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    cadastro.append(pessoas.copy())
    while True:
        resp = input('Continuar [S/N]? ').upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break
print('=' * 30)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas')
média = soma / len(cadastro)
print(f'B) A média das idades foi {média:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) As pessoas com idade acima da média foram ', end='')
for p in cadastro:
    if p['idade'] >= média:
        print('', end='')
        for k, v in p.items():
            print(f'{k}: {v} ', end='')
        print()
print('ENCERRADO')