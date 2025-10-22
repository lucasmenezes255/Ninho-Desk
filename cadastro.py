import json
import os
import re
import maskpass
from util import tracinho
from time import sleep

def carregar_dados():
    if not os.path.exists('dados_usuarios.json'): # Em caso de não existir o arquivo, retorna um dicionário vazio
        return {}
    with open('dados_usuarios.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def cadastrar_usuario():
    tracinho()
    while True:
        nome = str(input('Digite seu nome: ')).strip()
        if nome == '' or ' ' in nome[0]:
            print('\nERRO: Nome não pode ser vazio!')
            tracinho()
        elif nome[0] in '_-@!#%&*{[]}().':
            print('\nERRO: Nome não pode começar com caractere especial!')
            tracinho()
        elif '@#$%&*({[]})' in nome:
            print('\nERRO: Nome só pode conter (-_.) como caractere especial!')
            tracinho()
        elif nome[0] in '0123456789':
            print('\nNome não pode ser começar com números!')
            tracinho()
        else:
            break
    tracinho()
    email = str(input('\nDigite seu email: '))
    email = email_valido(email)
    tracinho()
    while True:
        senha = maskpass.askpass(prompt='Digite sua senha: ')
        tracinho()
        if senha == '':
            print('\nERRO: Senha não pode ser vazia!')
            tracinho()
        elif len(senha) < 8:
            print('\nERRO: Senha muito curta, deve ter pelo menos 8 caracteres!')
            tracinho()
        else:
            senha2 = maskpass.askpass(prompt='Confirme sua senha: ')
            if senha2!=senha:
                print('\nERRO: Senha digitada não correspode, tente novamente!')
                tracinho()
            else:
                break
    senha_mestre = senha_master()
    tracinho()
    serie_crianca = serie_valida()
    tracinho()
    print('Usuário cadastrado com sucesso!')
    sleep(1)
    dados_usuarios =  carregar_dados() # Carrega os dados existentes para dados_usuarios
    dados_usuarios[email] = {'Nome': nome, 'Série da Criança': serie_crianca, 'Senha': senha, 'Senha Mestre': senha_mestre} # O email cadastrado é a chave dos dados novos
    with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_usuarios, arquivo, indent=4, ensure_ascii=False)
    print ('\nUsuário cadastrado com sucesso!')

def senha_master():
    tracinho()
    while True:
        senha_mestre = maskpass.askpass(prompt='Digite a senha mestre: ')
        tracinho()
        if senha_mestre == '':
            print('\nERRO: Senha não pode ser vazia!')
            tracinho()
        elif len(senha_mestre) < 8:
            print('\nERRO: Senha muito curta, deve ter pelo menos 9 caracteres!')
            tracinho()
        elif not re.search('[a-zA-Z]', senha_mestre):
            print('\nERRO: A senha não possui letras')
            tracinho()
        elif not re.search('[0-9]', senha_mestre):
            print('\nERRO: A senha não possui números')
            tracinho()
        else:
            confirma = maskpass.askpass(prompt='Confirme sua senha: ')
            if confirma!= senha_mestre:
                print('\nERRO: Senha digitada não correspode, tente novamente')
                tracinho()
            else:
                return senha_mestre

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

def email_valido(email):
    dados = carregar_dados()
    formato_padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        if email in dados:
            print('\nERRO: Email já cadastrado! Tente novamente')
            email = str(input('Digite seu email: '))
            tracinho()
        else:
            while not re.fullmatch(formato_padrao, email):
                print ('\nERRO: Email inválido!')
                tracinho()
                email = str(input('Digite seu email: '))
                tracinho()
                email_valido(email)
                break
            return email
    
def serie_valida():
    while True:
        try:
            serie = int(input('Digite a série da criança: '))
        except:
            print('\nERRO: Informe uma série válida!')
            tracinho()
        else:
            if serie <1 or serie>9:
                print('\nERRO: Série inválida!')
                tracinho()
            else:
                return serie