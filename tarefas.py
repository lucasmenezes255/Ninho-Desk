from os import path
from datetime import datetime
import json
import re

def carregar_tarefas(email):
    if not path.exists('dados_tarefas.json'):
        dados = {email: {"Pendente": {'ALTA': [], 'MEDIA': [], 'BAIXA': [], 'SEM PRIORIDADE': []}, 
                         "Concluída": {'ALTA': [], 'MEDIA': [], 'BAIXA': [], 'SEM PRIORIDADE': []}}}
        with open('dados_tarefas.json', 'w', encoding='utf-8') as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)
        return dados
    else:
        with open('dados_tarefas.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
        if not email in dados:
            dados[email] = {"Pendente": {'ALTA': [], 'MEDIA': [], 'BAIXA': [], 'SEM PRIORIDADE': []}, 
                            "Concluída": {'ALTA': [], 'MEDIA': [], 'BAIXA': [], 'SEM PRIORIDADE': []}}
            with open('dados_tarefas.json', 'w', encoding='utf-8') as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)
            return dados
        return dados

class Tarefas:
    def __init__(self, email):
        self.email = email

    def conferir_tarefas(self):
        tarefas = carregar_tarefas(self.email)
        task = tarefas[self.email]
        return task
    
    def criar_tarefas(self, titulo, descricao, data, prioridade):
        formato_padrao = r'\d{2}/\d{2}/\d{4}'
        lista_prioridade = ['ALTA', 'MEDIA', 'BAIXA', 'SEM PRIORIDADE']
        if re.fullmatch(formato_padrao, data):
            data_time = datetime.strptime(data, '%d/%m/%Y')
            hoje = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        if titulo == "":
            return 0
        elif descricao == "" or ' ' in descricao[0]:
            return 1
        elif not re.fullmatch(formato_padrao, data):
            return 2
        elif data_time<hoje:
            return 3
        elif prioridade not in lista_prioridade:
            return 4
        else:
            return 5
   
    def salvar_tarefas(self, titulo, descricao, data, prioridade):
        tarefas = carregar_tarefas(self.email)
        tarefas[self.email]['Pendente'][prioridade].append({'Título': titulo, 'Descrição': descricao, 'Data': data, 'Prioridade': prioridade})
        with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
        
    def editar_titulo(self, titulo, novo_titulo):
        tarefas = carregar_tarefas(self.email)
        task = tarefas[self.email]
        for index, status in enumerate(task): 
            for indice, prioridade in enumerate(task[status]): 
                for quant_task in range(0, len(task[status][prioridade])):
                    if task[status][prioridade][quant_task]["Título"] == titulo:
                            task[status][prioridade][quant_task]["Título"] = novo_titulo
                            with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                                json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                            return True
        return False
    def editar_descricao(self, titulo, nova_descricao):
        tarefas = carregar_tarefas(self.email)
        task = tarefas[self.email]
        for index, status in enumerate(task): 
            for indice, prioridade in enumerate(task[status]): 
                for quant_task in range(0, len(task[status][prioridade])):
                    if task[status][prioridade][quant_task]["Título"] == titulo:
                            task[status][prioridade][quant_task]["Descrição"] = nova_descricao
                            with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                                json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                            return True
        return False
    def editar_prazo(self, titulo, novo_prazo):
        formato_padrao = r'\d{2}/\d{2}/\d{4}'
        if re.fullmatch(formato_padrao, novo_prazo):
            data_venc = datetime.strptime(novo_prazo, '%d/%m/%Y')
            hoje = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        tarefas = carregar_tarefas(self.email)
        task = tarefas[self.email]
        for index, status in enumerate(task): 
            for indice, prioridade in enumerate(task[status]): 
                for quant_task in range(0, len(task[status][prioridade])):
                    if task[status][prioridade][quant_task]["Título"] == titulo:
                        if not re.fullmatch(formato_padrao, novo_prazo):
                            return 0
                        elif data_venc<hoje:
                            return 1
                        else:
                            task[status][prioridade][quant_task]["Data"] = novo_prazo
                            with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                                json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                            return 2
        return 3
    def editar_prioridade(self, titulo, nova_prioridade):
        prioridades_lista = ['ALTA', 'MEDIA', 'BAIXA', 'SEM PRIORIDADE']
        tarefas = carregar_tarefas(self.email)
        task = tarefas[self.email]
        if nova_prioridade not in prioridades_lista:
            return False
        for index, status in enumerate(task): 
            for indice, prioridade in enumerate(task[status]): 
                for quant_task in range(0, len(task[status][prioridade])):
                    if task[status][prioridade][quant_task]["Título"] == titulo:
                        tarefa_copiada = task[status][prioridade][quant_task]
                        task[status][nova_prioridade].append(tarefa_copiada)
                        del tarefas[self.email][status][prioridade][quant_task]
                        with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                        return True
        return False

    def apagar_tarefa(self, titulo):
        tarefas = carregar_tarefas(self.email)
        task = tarefas[self.email]
        for index, status in enumerate(task): 
            for indice, prioridade in enumerate(task[status]): 
                for quant_task in range(0, len(task[status][prioridade])):
                    if task[status][prioridade][quant_task]["Título"] == titulo:
                        del task[status][prioridade][quant_task]
                        with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                        return True
        return False