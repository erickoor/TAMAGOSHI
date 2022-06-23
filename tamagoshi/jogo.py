import threading
from funçaomenu import *
from classeTamagoshi import Tamagoshi
from time import sleep
from sys import exit
from os import remove


cabeçalho('BICHINHO VIRTUAL')
bichinho = Tamagoshi()

try:
    open ('save.txt')
    print('Encotramos um jogo salvo. Deseja continuar ou iniciar um novo?')
    jogo = int(input('1 - Continuar  2 - Novo Jogo\n'))
    if jogo == 1:
        with open ('save.txt', 'r') as save:
            bichinho.nome = str(save.readline()).replace('\n', '')
            bichinho.fome = int(save.readline())
            bichinho.saude = int(save.readline())
            bichinho.idade = int(save.readline())
            bichinho.humor = int(save.readline())
    else:
        pass
except:
    bichinho.nome = str(input('Para iniciar, insira o nome do seu bichinho: '))
    with open ('save.txt', 'a') as save:
        save.write(str(f'{bichinho.nome}\n{bichinho.fome}\n{bichinho.saude}\n{bichinho.idade}\n{bichinho.humor}'))
    
#if jogo == 1:
    #print(dados_carregados.values)
    

contagem = threading.Thread(target = bichinho.vida)
contagem.daemon = True
contagem.start()  
print('Muito bem! Vamos começar!')
sleep(1)

while bichinho.saude > 0:
    escolha = menuJogo()
    if escolha == 1:
        bichinho.statusBichinho()
    elif escolha == 2:
        pass
    elif escolha == 3:
        pass
    elif escolha == 4:
        pass
    elif escolha == 5:
        bichinho.alterarNome()
    elif escolha == 8:
        cabeçalho('TCHAU! ESPERO TE VER EM BREVE')
        with open ('save.txt', 'w') as save:
            save.write(str(f'{bichinho.nome}\n{bichinho.fome}\n{bichinho.saude}\n{bichinho.idade}\n{bichinho.humor}'))
        exit()
else:
    remove('save.txt')
    cabeçalho('MORREU!')
    
    
    