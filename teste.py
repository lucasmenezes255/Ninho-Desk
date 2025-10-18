import json
import os

email = 'bruninho@gmail.com'

def carregar_dados():
    if not os.path.exists('dados_usuarios.json'): # Em caso de não existir o arquivo, retorna um dicionário vazio
        return {}
    with open('dados_usuarios.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

dados = carregar_dados()

if email in dados:
    print('sim')