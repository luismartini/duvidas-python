'''
Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra ‘FIM’, o
programa se encerrará. 
Importante: use cores.
'''
c=(
    '\033[m',        #0 sem cor
   '\033[0;30;41m',  #1 - vermelho
   '\033[7;30m',     #2 - 
   '\033[0;30;45m'   #3 - 
   '\033[1;30m',     #4 - Preto
   '\033[1;34m',     #5 - Azul
   '\033[1;96m',     #6 - Cyano
   );


def ajuda(com):
    help(com)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')

#PROGRAMA INICIAL
comando = ''
while True:    
    título('SISTEMA DE AJUDA PYHELP', 4)
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até logo!', 3)
