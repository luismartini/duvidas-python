galera = [['Jonice', 54], ['Luís', 44], ['Adele', 73], ['Carol', 41]]
print(galera[0])  #['Jonice', 54]
print(galera[0][0])  #Jonice
print(galera[2][1])  #73

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')