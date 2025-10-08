import json
import os
def carregar_dados():
    if not os.path.exists('dados_usuarios.json'): # Em caso de não existir o arquivo, retorna um dicionário vazio
        return {}
    with open('dados_usuarios.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def cadastrar_usuario():
    nome = str(input('Digite seu nome: '))
    email = str(input('Digite seu email: '))
    senha = str(input('Digite sua senha: '))
    serie_crianca = str(input('Digite a série da criança: '))
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

'''
Aqui tá somente o fluxo principal. Falta tratar os erros e validações:
- Verificar se já existe email cadastrado (FEITO)
- Verificar campo vazio
- Verificar se no campo de inserir o nome o usuário não digitou um número ou caractere especial
- Verificar se o email digitado é válido
- Confirmação de senha (FEITO)
- Verificar se a senha tem no mínimo 8 carac
- Verificar se a série da criança é um número válido (1 a 9)
- Esconder a senha digitada (Eu achei a biblioteca getpass, talvez funcione)
'''