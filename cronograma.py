from tarefas import carregar_tarefas
from datetime import datetime
import json
from util import limpar_tela, tracinho

def ver_cronograma(email):
    limpar_tela()
    with open('dados_tarefas.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
    if email not in dados:
          print('Nenhuma tarefa encontrada')
          return
    tarefas_usuario = dados[email]
    tarefas = (
          tarefas_usuario['ALTA']+
          tarefas_usuario['MEDIA']+
          tarefas_usuario['BAIXA']+
          tarefas_usuario['SEM PRIORIDADE']
    )
    if not tarefas:
        print('Nenhuma tarefa adicionada')
        return
    tarefas_cronograma = sorted(
        tarefas, key=lambda tarefa:datetime.strptime(tarefa['Data'], '%d/%m/%Y')
    )
    tracinho()
    print('Cronograma de tarefas\n')
    for tarefa in tarefas_cronograma:
        print(f"{tarefa['Data']}: {tarefa['Título']}")
    tracinho()
    input('Clique na tecla "Enter" para voltar')

def organizar_cronograma():
     