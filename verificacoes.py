from util import limpar_tela, tracinho
from time import sleep
from cadastro import carregar_dados, cadastrar_usuario, redefinir_senha, redefinir_senha_master
import maskpass

def verifica_senha(email, senha):
    limpar_tela()
    dados = carregar_dados()
    contador = 0
    while contador < 5:
        if dados[email]['Senha'] == senha:
            from main import menu_estudante
            menu_estudante(email)
            break
        else:
            limpar_tela()
            print('Senha incorreta, tente novamente!')
            senha = maskpass.askpass(prompt='Informe a sua senha: ')
            contador += 1
        if contador == 5:
            tracinho()
            print('Quantidade de tentativas expirada, crie uma nova senha!')
            tracinho()
            sleep(1)
            redefinir_senha(email)

def verifica_senha_master(email, senha):
    limpar_tela()
    dados = carregar_dados()
    contador = 0
    while contador < 5:
        if dados[email]['Senha Mestre'] == senha:
            return
        else:
            limpar_tela()
            print('\nERRO: Senha incorreta, tente novamente!')
            senha = maskpass.askpass(prompt='Informe a sua senha: ')
            contador += 1
        if contador == 5:
            tracinho()
            print('Quantidade de tentativas expirada, crie uma nova senha!')
            tracinho()
            sleep(1)
            limpar_tela()
            redefinir_senha_master(email)
            return

def verifica_email(email): 
    while True:
        limpar_tela()
        dados = carregar_dados()   
        if not email in dados:
            print('\nEmail inválido! Cadastre um novo usuário ou insira um email válido.\n')
            
            print('[1] Inserir um email válido')
            print('[2] Cadastrar um novo usuário')
            tracinho()
            escolha = str(input('Escolha uma opção acima: '))
            if  escolha == '1':
                tracinho()
                email = str(input('Insira um email válido: '))
                sleep(1)
            elif escolha == '2':
                limpar_tela()
                cadastrar_usuario()
                guia = 1
                break

            elif escolha == None:
                limpar_tela()
                print('ERRO: Informe uma escolha válida!') 
                tracinho()  
                sleep(1)                                       
            else:
                limpar_tela()
                print('ERRO: Opção inválida! Tente novamente!')
                tracinho()
                sleep(1)
        else:
            guia = 2
            break
    return guia, email

