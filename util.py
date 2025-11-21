import os
from time import sleep

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def tracinho():
    print('-'*40)

def pausa():
    sleep(2)
    limpar_tela()

def traco_igual():
    print('='*40)