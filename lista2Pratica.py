teste = list()
teste.append('Luís')
teste.append(44)

galera = list()
galera.append(teste[:])
teste[0] = 'Jonice'
teste[1] = 54
galera.append(teste[:])
# print(teste)
#print(galera)  #[['Jonice', 54], ['Jonice', 54]] ligação entre as estruturas
print(galera)  #[['Luís', 44], ['Jonice', 54]]