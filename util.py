import os 
from platform import system

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def tracinho():
    print('-'*40)
