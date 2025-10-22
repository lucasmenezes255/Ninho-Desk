import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def tracinho():
    print('-'*40)

limpar_tela()