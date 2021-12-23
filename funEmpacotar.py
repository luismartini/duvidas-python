#empacotamento
def contador(*núm):
    tamanho = len(núm)
    # for v in núm:
    #     print(f'{v} ', end='')  #vai criar uma tupla
    # print('Fim')
    print(f'Recebi os valores {núm} e são ao todo {tamanho}')



contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(1)

