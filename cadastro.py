import json
import os
import re
import maskpass
from util import tracinho, limpar_tela
from time import sleep

def carregar_dados():
    if not os.path.exists('dados_usuarios.json'): # Em caso de não existir o arquivo, retorna um dicionário vazio
        return {}
    with open('dados_usuarios.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def senha_master():
    tracinho()
    while True:
        senha_mestre = maskpass.askpass(prompt='Digite a senha mestre: ')
        if senha_mestre == '':
            print('Senha não pode ser vazia!')
        elif len(senha_mestre) < 8:
            print('Senha muito curta, crie uma senha de pelo menos 8 caracteres')
            tracinho()
        elif not re.search('[a-zA-Z]', senha_mestre):
            print('A senha não possui letras')
            tracinho()
        else:
            confirma = maskpass.askpass(prompt='Confirme sua senha: ')
            if confirma!= senha_mestre:
                print('Senha digitada não correspode, tente novamente')
                tracinho()
            else:
                return senha_mestre

def cadastrar_usuario():
    tracinho()
    while True:
        nome = str(input('Digite seu nome: ')).strip()
        if nome == '':
            print('Nome não pode ser vazio!')
            tracinho()
        elif ' ' in nome[0]:
            print('Nome não pode ser vazio!')
            tracinho()
        elif nome[0] in '0123456789':
            print('Nome não pode ser começar com números!')
            tracinho()
        else:
            break
    email = str(input('Digite seu email: '))
    email = email_valido(email)
    tracinho()
    while True:
        senha = maskpass.askpass(prompt='Digite sua senha: ')
        if senha == '':
            print('Senha não pode ser vazia!')
        elif len(senha) < 8:
            print('Senha muito curta, crie uma senha de pelo menos 8 caracteres')
        else:
            senha2 = maskpass.askpass(prompt='Confirme sua senha: ')
            if senha2!=senha:
                print('Senha digitada não correspode, tente novamente')
            else:
                break
    senha_mestre = senha_master()
    tracinho()
    serie_crianca = serie_valida()
    dados_usuarios =  carregar_dados() # Carrega os dados existentes para dados_usuarios
    dados_usuarios[email] = {'Nome': nome, 'Série da Criança': serie_crianca, 'Senha': senha, 'Senha Mestre': senha_mestre} # O email cadastrado é a chave dos dados novos
    with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_usuarios, arquivo, indent=4, ensure_ascii=False)
    print ('\nUsuário cadastrado com sucesso!')

def redefinir_senha_master(email):
    dados = carregar_dados()
    while True:
        nova_senha = maskpass.askpass(prompt='Digite a senha mestre: ')
        if nova_senha == '':
            print('Senha não pode ser vazia!')
        elif len(nova_senha) < 8:
            print('Senha muito curta, crie uma senha de pelo menos 8 caracteres')
            tracinho()
        elif not re.search('[a-zA-Z]', nova_senha):
            print('A senha não possui letras')
            tracinho()
        else:
            confirma = maskpass.askpass(prompt='Confirme sua senha: ')
            if confirma!= nova_senha:
                print('Senha digitada não correspode, tente novamente')
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
        if nova_senha == '':
            print('Senha não pode ser vazia!')
        elif len(nova_senha) < 8:
            print('Senha muito curta, crie uma senha de pelo menos 8 caracteres')
        else:
            nova_senha2 = maskpass.askpass(prompt='Confirme sua nova senha: ')
            if nova_senha2!= nova_senha:
                print('Senha digitada não corresponde, tente novamente')
            else:
                break    
    tracinho()
    print('Senha redefinida com sucesso')
    dados[email]['Senha'] = nova_senha
    with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def email_valido(email):
    dados = carregar_dados()
    formato_padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        if email in dados:
            print('Email já cadastrado! Tente novamente')
            email = str(input('Digite seu email: '))
        else:
            while not re.fullmatch(formato_padrao, email):
                print ('Email inválido!')
                email = str(input('Digite seu email: '))
            return email
    
def serie_valida():
    while True:
        try:
            serie = int(input('Digite a série da criança: '))
        except:
            print('ERRO: Informe uma série válida!')
            tracinho()
        else:
            if serie <1 or serie>9:
                print('ERRO: Série inválida!')
                tracinho()
            else:
                return serie