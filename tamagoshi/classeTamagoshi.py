
from time import sleep
from funçaomenu import *
from random import randint
import threading

class Tamagoshi:
    def __init__(self, nome='', fome=randint(0, 10), saude=10, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = 0
        
    def alterarNome(self):
        cabeçalho('ALTERAÇÂO DO NOME')
        self.nome = str(input('Insira o novo nome: '))
        print('Nome alterado com sucesso!')
        sleep(1)
    
    def alimentar(self):
        pass
    
    def darRemedio(self):
        pass
    
    def statusBichinho(self):
        cabeçalho('STATUS DO SEU BICHINHO')
        print(f'\033[36mNome do Bichinho: {self.nome}     \t\tNível de Fome: {self.fome}')
        print(f'Estado de Saúde: {self.saude}     \t\t\tNível de Humor: {self.humor}\033[m')
        sleep(2)
    
    def vida(self):     
        tempo = 0
        while self.saude > 0:
            tempo += 1
            sleep(1)
            if tempo % 1 == 0:
                self.saude -= 1
