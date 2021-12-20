galera = list()
dado = list()  #É necessário haver uma estrutura auxiliar
totmai = totmen = 0

for c in range(0, 3):  #capturar dados
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  #cópia profunda
    dado.clear()
#print(galera)  #[['Luís', 44], ['Jonice', 54], ['Adele', 73], ['Carol', 41], ['Dudu', 11]]

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
        
print(f'Temos {totmai} maior e {totmen} menores')
