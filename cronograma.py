from tarefas import carregar_tarefas
from datetime import datetime
from util import Util
from time import sleep
from lembretes import Lembrete
import json
import os

def carregar_cronograma():
    if not os.path.exists('cronograma.json'):
        return {}
    with open('cronograma.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados
class Cronograma(Lembrete):
    def __init__(self, email):
        self.email = email

    def ver_cronograma_tarefas(self):
        dados = carregar_tarefas(self.email)
        if self.email not in dados:
            return 0
        else:
            tarefas_usuario = dados[self.email]
            tarefas = (
                tarefas_usuario['Pendente']['ALTA']+
                tarefas_usuario['Pendente']['MEDIA']+
                tarefas_usuario['Pendente']['BAIXA']+
                tarefas_usuario['Pendente']['SEM PRIORIDADE']
            )
        if not tarefas:
            return 1
        else:
            tarefas_cronograma = sorted(
                tarefas, key=lambda tarefa:datetime.strptime(tarefa['Data'], '%d/%m/%Y')
            )
            return tarefas_cronograma
        
    def ver_cronograma_estudos(self):
        cronograma = carregar_cronograma()
        if not self.email in cronograma:
            return 0
        else: 
            lista = cronograma[self.email]
            return lista

    def add_cronograma(self, lista_cronograma):
        segunda = lista_cronograma[0]
        terca = lista_cronograma[1]
        quarta = lista_cronograma[2]
        quinta = lista_cronograma[3]
        sexta = lista_cronograma[4]
        sabado = lista_cronograma[5]
        domingo = lista_cronograma[6]
        cronograma = carregar_cronograma()
        if self.email not in cronograma:
            cronograma[self.email] = []
        cronograma[self.email] = {"Segunda-Feira": segunda, 
                            "Terça-Feira": terca, 
                            "Quarta-Feira": quarta, 
                            "Quinta-Feira": quinta, 
                            "Sexta-Feira": sexta, 
                            "Sábado": sabado, 
                            "Domingo": domingo}
        self.salvar_cronograma(cronograma)
    
    @staticmethod
    def salvar_cronograma(cronograma):
        with open('cronograma.json', 'w', encoding=  'utf-8') as arquivo:
            json.dump(cronograma, arquivo, indent=4, ensure_ascii=False)