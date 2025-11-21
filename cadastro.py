import json
import os
import re
import maskpass
from util import tracinho
from time import sleep
from util import limpar_tela, pausa, traco_igual
from time import sleep

def carregar_dados():
    if not os.path.exists('dados_usuarios.json'): # Em caso de não existir o arquivo, retorna um dicionário vazio
        return {}
    with open('dados_usuarios.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados
class Usuario:
    def __init__(self):
        self.nome = ''
        self.email = ''
        self.serie_crianca = ''
        self.__senha = ''
        self.__senha_mestre = ''

    def validar_username(self):
        tracinho()
        self.nome = str(input('Insira o seu nome: '))
        while True:
            if self.nome == '' or ' ' in self.nome[0]:
                print('\nERRO: Nome não pode ser vazio!')
                tracinho()
                self.nome = str(input('Insira o seu nome: '))
            elif self.nome[0] in '_-@!#%&*{[]}().':
                print('\nERRO: Nome não pode começar com caractere especial!')
                tracinho()
                self.nome = str(input('Insira o seu nome: '))
            elif '@#$%&*({[]})' in self.nome:
                print('\nERRO: Nome só pode conter (-_.) como caractere especial!')
                tracinho()
                self.nome = str(input('Insira o seu nome: '))
            elif self.nome[0] in '0123456789':
                print('\nNome não pode ser começar com números!')
                tracinho()
                self.nome = str(input('Insira o seu nome: '))
            else:
                break
        self.validar_email()

    def validar_email(self):
        dados = carregar_dados()
        formato_padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.email = str(input('\nDigite seu email: '))
        while True:
            if self.email in dados:
                print('\nERRO: Email já cadastrado! Tente novamente')
                self.email = str(input('Digite seu email: '))
                tracinho()
            else:
                while not re.fullmatch(formato_padrao, self.email):
                    print ('\nERRO: Email inválido!')
                    tracinho()
                    self.email = str(input('\nDigite seu email: '))
                    tracinho()
                    self.email = self.verificar_email()
                    break
                break
        self.cadastrar_senha()

    def cadastrar_senha(self):
        while True:
            self.__senha = maskpass.askpass(prompt='Digite sua senha: ')
            tracinho()
            if self.__senha == '':
                print('\nERRO: Senha não pode ser vazia!')
                pausa()
                tracinho()
            elif len(self.__senha) < 8:
                print('\nERRO: Senha muito curta, deve ter pelo menos 8 caracteres!')
                pausa()
                tracinho()
            else:
                senha_validadora = maskpass.askpass(prompt='Confirme sua senha: ')
                if senha_validadora != self.__senha:
                    print('\nERRO: Senha digitada não correspode, tente novamente!')
                    pausa()
                    tracinho()
                else:
                    break
        self.cadastrar_senha_mestre()

    def cadastrar_senha_mestre(self):
        traco_igual()
        while True:
            self.__senha_mestre = maskpass.askpass(prompt='Digite a senha mestre: ')
            tracinho()
            if self.__senha_mestre == '':
                print('\nERRO: Senha não pode ser vazia!')
                tracinho()
            elif len(self.__senha_mestre) < 8:
                print('\nERRO: Senha muito curta, deve ter pelo menos 9 caracteres!')
                tracinho()
            elif not re.search('[a-zA-Z]', self.__senha_mestre):
                print('\nERRO: A senha não possui letras')
                tracinho()
            elif not re.search('[0-9]', self.__senha_mestre):
                print('\nERRO: A senha não possui números')
                tracinho()
            else:
                confirmacao = maskpass.askpass(prompt='Confirme sua senha: ')
                if confirmacao != self.__senha_mestre:
                    print('\nERRO: Senha digitada não correspode, tente novamente')
                    tracinho()
                else:
                    break 
        self.cadastrar_serie()

    def cadastrar_serie(self):
        traco_igual()
        while True:
            try:
                self.serie_crianca = int(input('Digite a série da criança: '))
            except:
                print('\nERRO: Informe uma série válida!')
                tracinho()
            else:
                if self.serie_crianca <1 or self.serie_crianca>9:
                    print('\nERRO: Série inválida!')
                    tracinho()
                else:
                    break
        self.salvar_dados()

    def salvar_dados(self):
        dados_usuarios =  carregar_dados() # Carrega os dados existentes para dados_usuarios
        dados_usuarios[self.email] = {'Nome': self.nome, 'Série da Criança': self.serie_crianca, 'Senha': self.__senha, 'Senha Mestre': self.__senha_mestre} # O email cadastrado é a chave dos dados novos
        with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados_usuarios, arquivo, indent=4, ensure_ascii=False)
        print ('\nUsuário cadastrado com sucesso!')

def redefinir_senha_master(email):
    dados = carregar_dados()
    while True:
        nova_senha = maskpass.askpass(prompt='Digite a senha mestre: ')
        if nova_senha == '':
            print('\nERRO: Senha não pode ser vazia!')
        elif len(nova_senha) < 8:
            print('\nERRO: Senha muito curta, deve ter pelo menos 8 caracteres')
            tracinho()
        elif not re.search('[a-zA-Z]', nova_senha):
            print('\nERRO: A senha não possui letras')
            tracinho()
        elif not re.search('[0-9]', nova_senha):
            print('\nERRO: A senha não possui números')
            tracinho()
        else:
            confirma = maskpass.askpass(prompt='Confirme sua senha: ')
            if confirma!= nova_senha:
                print('\nERRO: Senha digitada não correspode, tente novamente')
                tracinho()
            else:
                break
    tracinho()
    print('Senha redefinida com sucesso')
    dados[email]['Senha Mestre'] = nova_senha
    with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def redefinir_senha(email):
    dados = carregar_dados()
    while True:
        nova_senha = maskpass.askpass(prompt='Digite sua nova senha: ')
        tracinho()
        if nova_senha == '':
            print('\nERRO: Senha não pode ser vazia!')
        elif len(nova_senha) < 8:
            print('\nERRO: Senha muito curta, crie uma senha de pelo menos 8 caracteres')
        else:
            nova_senha2 = maskpass.askpass(prompt='Confirme sua nova senha: ')
            tracinho()
            if nova_senha2!= nova_senha:
                print('\nERRO: Senha digitada não corresponde, tente novamente')
            else:
                break    
    tracinho()
    print('Senha redefinida com sucesso')
    tracinho()
    print('Voltando')
    dados[email]['Senha'] = nova_senha
    with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    for i in range(3):
        print('.')
        sleep(1)
