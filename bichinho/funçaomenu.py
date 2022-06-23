from time import sleep

def linha():
    print('='*60)

def cabeçalho(msg):
    print('\033[32m='*60)
    print(f'{msg:^60}')
    print('='*60 + '\033[m')
    
def menuJogo():
    cabeçalho('MENU DE OPÇÕES')
    print('\033[33m1 - Ver Status   2 - Alimentar  3 - Brincar  4 - Dar Remédio')
    print('5 - Alterar Nome  8 - Sair\033[m')
    linha()
    opcao = int(input('O que vamos fazer? '))
    return opcao


