import os
from time import sleep

class Util: 
    def __init__(self):
        pass
        
    def limpar_tela():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def tracinho():
        print('-'*40)

    def pausa():
        sleep(2)
        Util.limpar_tela()

    def traco_igual():
        print('='*40)