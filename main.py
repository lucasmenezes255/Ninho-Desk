from cadastro import cadastrar_usuario, carregar_dados, redefinir_senha
from util import tracinho, limpar_tela
import maskpass
   
def menu_estudante():
    limpar_tela()
    print('='*40)
    print(f'{'[MENU]':=^40}')
    print('='*40)
    print('[1] Conferir Tarefas\n[2] Ver Cronograma\n[3] Ver Lembretes\n[4] Pet Virtual\n[5] Controle dos Pais')
    escolha_menu=str(input('\n Selecione uma opção: '))
    while True:
        if escolha_menu=='1':
        elif escolha_menu=='2':       #Aqui pra redirecionar para as respectivas funções quando estiverem prontas
        elif escolha_menu=='3':
        elif escolha_menu=='4':
        elif escolha_menu=='5':
        else:
            print ('Opção inválida! Tente novamente')
            print('[1] Conferir Tarefas\n[2] Ver Cronograma\n[3] Ver Lembretes\n[4] Pet Virtual\n[5] Controle dos Pais')
            escolha_menu=str(input('\n Selecione uma opção: '))

def verifica_email(email): 
    dados = carregar_dados()   
    if not email in dados:
        print('\nEmail inválido! Cadastre um novo usuário ou insira um email válido.\n')
       
        while True:
            print('[1] Inserir um email válido')
            print('[2] Cadastrar um novo usuário')
            tracinho()
            escolha = str(input('Escolha uma opção acima: '))
            if  escolha == '1':
                tracinho()
                email = str(input('Insira um email válido: '))
                verifica_email(email)
                break
            elif escolha == '2':
                cadastrar_usuario()
                break 
            elif escolha == None:
                print('Informe uma escolha válida')                                            
            else:
                print('Opção inválida! Tente novamente!')
            

def verifica_senha(email, senha):
    dados = carregar_dados()
    contador = 0
    while contador < 4:
        if dados[email]['Senha'] == senha:
            menu_estudante()
            break
        else:
            print('Senha incorreta, tente novamente!')
            senha = maskpass.askpass(prompt='Informe a sua senha: ')
            contador += 1
        if contador == 4:
            tracinho()
            print('Quantidade de tentativas expirada, crie uma nova senha!')
            tracinho()
            redefinir_senha(email)

def login():
    dados = carregar_dados()
    tracinho()
    print('Seja bem-vindo ao Ninho Desk🦉\nSeu APP de gerenciamento acadêmico!\nVamos iniciar?')
    tracinho()
    print('[1] Login')
    print('[2] Cadastrar novo usuário')
    tracinho()
    while True:
        try:
            escolha = int(input('Escolha uma opção: '))
        except:
            print('Informe uma escolha válida')
        else:
            break

    while True:
        if escolha == 1:
            limpar_tela()
            tracinho()
            email = str(input('Informe o email de login: '))
            verifica_email(email)
            while True:
                tracinho()
                print('[1] Informe a senha')
                print('[2] Esqueceu a senha')
                while True:
                    try:
                        escolha = int(input('\nEscolha uma opção acima: '))
                    except:
                        print('Informe uma escolha válida')
                    else:
                        break
                if escolha == 1:
                    tracinho()
                    senha = maskpass.askpass(prompt='Informe a sua senha: ')
                    verifica_senha(email, senha)
                    break
                elif escolha == 2:
                    tracinho()
                    redefinir_senha(email)
                    break
                else:
                    print('Opção inválida! Tente novamente!')
            break
        elif escolha == 2:
            limpar_tela()
            cadastrar_usuario()
            break
        else:
            print('Opção inválida! Tente novamente!')
login()

'''
Pensar em uma forma de criar uma função pra testar o erro de campo vazio
'''