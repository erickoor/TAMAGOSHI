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
    print('\033[35mEncotramos um jogo salvo. Deseja continuar ou iniciar um novo?')
    jogo = int(input('1 - Continuar  2 - Novo Jogo\n\033[m'))
    if jogo == 1:
        with open ('save.txt', 'r') as save:
            bichinho.nome = str(save.readline()).replace('\n', '')
            bichinho.fome = int(save.readline())
            bichinho.saude = int(save.readline())
            bichinho.idade = int(save.readline())
            bichinho.humor = int(save.readline())
    else:
        bichinho.nome = str(input('Para iniciar, insira o nome do seu bichinho: '))
    with open ('save.txt', 'a') as save:
        save.write(str(f'{bichinho.nome}\n{bichinho.fome}\n{bichinho.saude}\n{bichinho.idade}\n{bichinho.humor}'))
except:
    bichinho.nome = str(input('Para iniciar, insira o nome do seu bichinho: '))
    with open ('save.txt', 'a') as save:
        save.write(str(f'{bichinho.nome}\n{bichinho.fome}\n{bichinho.saude}\n{bichinho.idade}\n{bichinho.humor}'))
        
contagem_fome = threading.Thread(target = bichinho.contagemFome)
contagem_fome.daemon = True
contagem_saude = threading.Thread(target = bichinho.contagemSaude)
contagem_saude.daemon = True
contagem_humor = threading.Thread(target = bichinho.contagemHumor)
contagem_humor.daemon = True

contagem_fome.start()
contagem_saude.start()
contagem_humor.start()
  
print('Muito bem! Vamos começar!')
sleep(1)
while bichinho.saude > 0 and bichinho.idade < 15:
    escolha = menuJogo()
    if escolha == 1:
        bichinho.statusBichinho()
    elif escolha == 2:
        bichinho.alimentar()
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
    if bichinho.saude == 0:
        remove('save.txt')
        cabeçalho('\033[31mSEU BICHINHO ESTÁ MORTO! SUA SAÚDE CHEGOU A ZERO(0)! \nSEU IRRESPONSÁVEL!\033[m')       
    else:
        remove('save.txt')
        cabeçalho('\033[31mSEU BICHINHO FALECEU! ELE ATINGIU A IDADE MÁXIMA DE 15 ANOS! \nDESCANSE EM PAZ\033[m')
            
    
    
    