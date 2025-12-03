import json
import os

def carregar_lembretes():
    if not os.path.exists('lembretes.json'):
        return {}
    with open('lembretes.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

class Lembrete:
    def __init__(self, email):
        self.email = email

    def add_lembretes(self, titulo, descricao):
        lembretes = carregar_lembretes()
        if self.email not in lembretes:
            lembretes[self.email] = []
        lembretes[self.email].append({'Título': titulo, 'Descrição': descricao})
        self.salvar_lembretes(lembretes)
            
    @staticmethod
    def salvar_lembretes(lembretes):
        with open('lembretes.json', 'w', encoding=  'utf-8') as arquivo:
            json.dump(lembretes, arquivo, indent=4, ensure_ascii=False)

    def lista_lembretes(self):
        lembretes = carregar_lembretes()
        if self.email not in lembretes or len(lembretes)==0:
            return 0
        elif len(lembretes) >= 1:
            return 1