from util import Util
from time import sleep
from cadastro import carregar_dados, Usuario
import maskpass

class Verificacao(Usuario):
    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return f"{self.email}"
     
    def verifica_email_login(self):
        dados = carregar_dados()
        while True:
            if self.email not in dados:
                print('\nEmail inválido! Cadastre um novo usuário ou insira um email válido.\n')

                print('[1] Inserir um email válido')
                print('[2] Cadastrar um novo usuário')
                Util.tracinho()
                escolha = str(input('Escolha uma opção acima: '))
                if escolha == '1':
                    self.email = str(input('Insira um email válido: '))
                    sleep(1)
                elif escolha == '2':
                    self.validar_username()
                    break
                elif escolha == None:
                    Util.limpar_tela()
                    print('ERRO: Informe uma escolha válida!') 
                    Util.tracinho()  
                    sleep(1)                                       
                else:
                    Util.limpar_tela()
                    print('ERRO: Opção inválida! Tente novamente!')
                    Util.tracinho()
                    sleep(1)
            else:
                break

    def verificar_senha(self):
        Util.limpar_tela()
        dados = carregar_dados()
        Util.tracinho()
        senha = maskpass.askpass(prompt='Informe a sua senha: ')
        contador = 0
        while contador < 5:
            if dados[self.email]['Senha'] == senha:
                return
            else:
                Util.limpar_tela()
                print('Senha incorreta, tente novamente!')
                senha = maskpass.askpass(prompt='Informe a sua senha: ')
                contador += 1
            if contador == 5:
                Util.tracinho()
                print('Quantidade de tentativas expirada, crie uma nova senha!')
                Util.tracinho()
                sleep(1)
                self.redefinir_senha()
                return

    def verificar_senha_master(self):
        Util.limpar_tela()
        dados = carregar_dados()
        senha = maskpass.askpass(prompt='Informe a sua senha: ')
        contador = 0
        while contador < 5:
            if dados[self.email]['Senha Mestre'] == senha:
                return
            else:
                Util.limpar_tela()
                print('\nERRO: Senha incorreta, tente novamente!')
                senha = maskpass.askpass(prompt='Informe a sua senha: ')
                contador += 1
            if contador == 5:
                Util.tracinho()
                print('Quantidade de tentativas expirada, crie uma nova senha!')
                Util.tracinho()
                sleep(1)
                Util.limpar_tela()
                self.redefinir_senha_master()
                return