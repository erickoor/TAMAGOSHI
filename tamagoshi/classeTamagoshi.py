from time import sleep
from funçaomenu import *
from random import randint

class Tamagoshi:
    def __init__(self, nome='', fome=randint(0, 10), saude=10, idade=0, humor=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = humor
        
    def alterarNome(self):
        cabeçalho('ALTERAÇÂO DO NOME')
        self.nome = str(input('Insira o novo nome: '))
        print('Nome alterado com sucesso!')
        sleep(1)
    
    def alimentar(self):
        opcao = 0
        while opcao < 6:
            cabeçalho('HORA DE COMER')
            print('\033[33m1 - Hamburguer   2 - Pastel  3 - Pizza  4 - Salada')
            print('5 - Frutas  6 - Sair\033[m')
            linha()
            opcao = int(input('O QUE EU VOU COMER? \n'))
            if self.fome >= 10:
                self.fome = 10
                print('\033[33mESTOU CHEIO, NÃO QUERO MAIS COMER!\033[m')
                break
            elif opcao == 1: #hamburguer
                print('\033[36mESTAVA UMA DELÍCIA!\033[m')
                self.fome += 5
                self.humor +=2
                self.saude -= 3
                sleep(1)
            elif opcao == 2: #pastel
                print('\033[36mESTAVA UMA DELÍCIA!\033[m')
                self.fome += 3
                self.saude -= 4
                self.humor +=2
                sleep(1)
            elif opcao == 3: #pizza
                print('\033[36mESTAVA UMA DELÍCIA!\033[m')
                self.fome += 4
                self.saude -= 3
                self.humor +=3
                sleep(1)
            elif opcao == 4: #salada
                print('\033[36mESTAVA UMA DELÍCIA!\033[m')
                self.fome += 1
                if self.saude < 10:
                    self.saude += 3
                else:
                    self.saude = 10
                sleep(1)
            elif opcao == 5: #Frutas
                print('\033[36mESTAVA UMA DELÍCIA!\033[m')
                self.fome += 2
                self.humor +=2
                if self.saude < 10:
                    self.saude += 3
                else:
                    self.saude = 10
                sleep(1)
        print('O QUE VAMOS FAZER AGORA?')
        sleep(1)
        
    def darRemedio(self):
        pass
    
    def statusBichinho(self):
        cabeçalho('STATUS DO SEU BICHINHO')
        print(f'\033[36mNome do Bichinho: {self.nome}     \t\tNível de Fome: {self.fome}')
        print(f'Estado de Saúde: {self.saude}     \t\t\tNível de Humor: {self.humor}')
        print(f'Anos de Idade: {self.idade}\033[m')
        linha()
        if self.fome < 5:
            print('\033[33mESTOU COM MUITA FOME! ME DE ALGUMA COMIDA!\033[m')
        if self.humor < 5:
            print('\033[33mESTOU IMPACIENTE! QUERO BRINCAR!\033[m')
        if self.saude < 5:
            print('\033[33mACHO QUE NÂO ESTOU ME SENTINDO MUITO BEM, PRECISO DE UM MÉDICO\033[m')
        sleep(2)
    
    def contagemSaude(self):     
        tempo = 0
        while self.saude > 0:
            tempo += 1
            sleep(1)
            if tempo % 10 == 0:
                self.saude -= 1
                
    def contagemFome(self):
        tempo = 0
        while self.fome > 0:
            tempo += 1
            sleep(1)
            if tempo % 10 == 0:
                self.fome -= 1
                
    def contagemHumor(self):
        tempo = 0
        while self.humor > 0:
            tempo += 1
            sleep(1)
            if tempo % 10 == 0:
                self.humor -= 1
