import json
import os

email = 'bruninho@gmail.com'

def carregar_dados():
    if not os.path.exists('dados_usuarios.json'): # Em caso de não existir o arquivo, retorna um dicionário vazio
        return {}
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

dados = carregar_dados()

dicionario = {
    "teste1@gmail.com": {
        "ALTA": [
            {
                "Título": "Primeira tarefa",
                "Descrição": "essa é a primeira tarefa construída, espero que rode certinho o código e não dê falha",
                "Prioridade": "ALTA"
            }
        ],
        "MEDIA": [],
        "BAIXA": [],
        "SEM PRIORIDADE": [
            {
                "Título": "Teste pra visualizar as tarefas",
                "Descrição": "Essa task é pra testar se vai mostrar as tarefas direiinho e o que tem pra mudar nelas",
                "Prioridade": "SEM_PRIORIDADE"
            }
        ]
    }
}

for i, v in enumerate(dicionario):
    print(i)