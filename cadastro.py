import json
import os

def carregar_dados():
    if not os.path.exists('dados.json'): # Em caso de não existir o arquivo, retorna um dicionário vazio
        return {}
    with open('dados.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def cadastrar_usuario():
    nome = str(input('Digite seu nome: '))
    email = str(input('Digite seu email: '))
    senha = str(input('Digite sua senha: '))
    serie_crianca = str(input('Digite a série da criança: '))
    dados_string = carregar_dados() # Carrega os dados existentes para dados_string
    dados_string[email] = {'Nome': nome, 'Série da Criança': serie_crianca, 'Senha': senha} # O email cadastrado é a chave dos dados novos
    with open('dados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_string, arquivo, indent=4, ensure_ascii=False)

cadastrar_usuario()

'''
Aqui tá somente o fluxo principal. Falta tratar os erros e validações:
- Verificar se já existe email cadastrado
- Verificar campo vazio
- Verificar se no campo de inserir o nome o usuário não digitou um número ou caractere especial
- Verificar se o email digitado é válido
- Confirmação de senha
- Verificar se a senha tem no mínimo 8 carac
- Verificar se a série da criança é um número válido (1 a 9)
- Esconder a senha digitada (Eu achei a biblioteca getpass, talvez funcione)
'''