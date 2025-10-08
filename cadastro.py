import json
import os
import re 

def carregar_dados():
    if not os.path.exists('dados_usuarios.json'): # Em caso de não existir o arquivo, retorna um dicionário vazio
        return {}
    with open('dados_usuarios.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def cadastrar_usuario():
    nome = str(input('Digite seu nome: '))
    email = str(input('Digite seu email: '))
    email_valido(email)
    senha = str(input('Digite sua senha: '))
    serie_crianca = int(input('Digite a série da criança: '))
    serie_valida(serie_crianca)
    dados_usuarios =  carregar_dados() # Carrega os dados existentes para dados_usuarios
    dados_usuarios[email] = {'Nome': nome, 'Série da Criança': serie_crianca, 'Senha': senha} # O email cadastrado é a chave dos dados novos
    with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_usuarios, arquivo, indent=4, ensure_ascii=False)

def redefinir_senha(email):
    dados = carregar_dados()
    nova_senha = str(input('Digite uma nova senha: '))
    dados[email]['Senha'] = nova_senha
    with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print('Senha redefinida com sucesso')

def email_valido(email):
    formato_padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while not re.fullmatch(formato_padrao, email):
        print ('Email inválido')
        email = str(input('Digite seu email: '))
        
def serie_valida(serie_crianca):
    while serie_crianca<1 or serie_crianca>9:
        print('Série inválida')
        serie_crianca = int(input('Digite a série da criança: '))
        

'''
Aqui tá somente o fluxo principal. Falta tratar os erros e validações:
- Verificar se já existe email cadastrado (FEITO)
- Verificar campo vazio
- Verificar se no campo de inserir o nome o usuário não digitou um número ou caractere especial
- Verificar se o email digitado é válido (FEITO)
- Confirmação de senha (FEITO)
- Verificar se a senha tem no mínimo 8 carac
- Verificar se a série da criança é um número válido (1 a 9) (FEITO)
- Esconder a senha digitada (Eu achei a biblioteca getpass, talvez funcione) #pelo que vi é literalmente esconder kkkkkk
'''