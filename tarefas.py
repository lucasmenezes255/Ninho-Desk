from util import limpar_tela, tracinho
from os import path
from time import sleep
from rich.table import Table
from rich.console import Console
from datetime import datetime
import json
import re

def carregar_tarefas(email):
    if not path.exists('dados_tarefas.json'):
        dados = {email: {'ALTA': [], 'MEDIA': [], 'BAIXA': [], 'SEM PRIORIDADE': []}}
        with open('dados_tarefas.json', 'w', encoding='utf-8') as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)
        return dados
    else:
        with open('dados_tarefas.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
        if not email in dados:
            dados[email] = {'ALTA': [], 'MEDIA': [], 'BAIXA': [], 'SEM PRIORIDADE': []}
            with open('dados_tarefas.json', 'w', encoding='utf-8') as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)
            return dados
        return dados

def editar_tarefas(email):
    limpar_tela()
    tarefas = carregar_tarefas(email)
    print('='*40)
    print(f'{"LISTA DE TAREFAS":^40}')
    print('='*40)
    tracinho()
    task = tarefas[email]
    quantidade_task = len(task["ALTA"]) + len(task["MEDIA"]) + len(task["BAIXA"]) + len(task["SEM PRIORIDADE"])
    if quantidade_task == 0:
        print('')
        print('Sem tarefas!')
        sleep(1)
        administrar_tarefas(email)
        return
    else:
        for i in range(0, len(task)): 
            if i == 0:
                while True:
                    for quant_task in range(0, len(task["ALTA"])):
                        print(f'{i+1}. Título: {task["ALTA"][quant_task]["Título"]}\n   Descrição: {task["ALTA"][quant_task]["Descrição"]}\n   Prioridade: {task["ALTA"][quant_task]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 1:
                while True:
                    for quant_task in range(0, len(task["MEDIA"])):
                        print(f'{i+1}. Título: {task["MEDIA"][quant_task]["Título"]}\n   Descrição: {task["MEDIA"][quant_task]["Descrição"]}\n   Prioridade: {task["MEDIA"][quant_task]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 2:
                while True:
                    for quant_task in range(0, len(task["BAIXA"])):
                        print(f'{i+1}. Título: {task["BAIXA"][quant_task]["Título"]}\n   Descrição: {task["BAIXA"][quant_task]["Descrição"]}\n   Prioridade: {task["BAIXA"][quant_task]["Prioridade"]}')
                        tracinho()  
                    break
            elif i == 3:
                while True:
                    for quant_task in range(0, len(task["SEM PRIORIDADE"])):
                        print(f'{i+1}. Título: {task["SEM PRIORIDADE"][quant_task]["Título"]}\n   Descrição: {task["SEM PRIORIDADE"][quant_task]["Descrição"]}\n   Prioridade: {task["SEM PRIORIDADE"][quant_task]["Prioridade"]}')
                        tracinho()  
                    break
        console = Console()
        tabela = Table(title='QUANTIDADE DE TAREFAS POR PRIORIDADE')
        tabela.add_column('Alta', style='red', justify='center')
        tabela.add_column('Média', style='yellow', justify='center')
        tabela.add_column('Baixa', style='green', justify='center')
        tabela.add_column('Sem Prioridade', style='black', justify='center')
        tabela.add_row(str(len(task["ALTA"])), str(len(task["MEDIA"])), str(len(task["BAIXA"])), str(len(task["SEM PRIORIDADE"])))
        console.print(tabela)
        while True:
            print('='*40)
            print(f'{"MENU DE EDIÇÕES":^40}')
            print('='*40)
            print('[1] Mover Tarefa\n'
                  '[2] Apagar Tarefa\n' 
                  '[3] Alterar Tarefa\n' 
                  '[4] Sair')
            while True:  
                try:
                    escolha = int(input('Escolha uma opção: '))
                except:
                    print('Informação inválida! Selecione um valor do menu')
                else:
                    if escolha not in [1, 2, 3, 4]:
                        print('Informação inválida! Selecione um valor do menu')
                    else:
                        break
            if escolha == 1:
                print('')
            elif escolha == 2:
                titulo_tarefa = str(input('Informe o título da tarefa que desejar apagar: '))
                for i in range(0, len(task)): 
                    if i == 0:
                        for index in range(0, len(task["ALTA"])):
                            if task["ALTA"][index]["Título"] == titulo_tarefa:
                                del tarefas[email]["ALTA"][index]
                                tracinho()
                                print('Tarefa apagada com sucesso!')
                                break
                        with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                    elif i == 1:
                        for index in range(0, len(task["MEDIA"])):
                            if task["MEDIA"][index]["Título"] == titulo_tarefa:
                                del tarefas[email]["ALTA"][index]
                                tracinho()
                                print('Tarefa apagada com sucesso!')
                                break
                        with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                    elif i == 2:
                        for index in range(0, len(task["BAIXA"])):
                            if task["BAIXA"][index]["Título"] == titulo_tarefa:
                                del tarefas[email]["ALTA"][index]
                                tracinho()
                                print('Tarefa apagada com sucesso!')
                                break
                        with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                    elif i == 3:
                        for index in range(0, len(task["SEM PRIORIDADE"])):
                            if task["SEM PRIORIDADE"][index]["Título"] == titulo_tarefa:
                                del tarefas[email]["ALTA"][index]
                                tracinho()
                                print('Tarefa apagada com sucesso!')
                                break
                        with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
            elif escolha == 3:
                print('')
            elif escolha == 4:
                from main import controle_pais
                controle_pais(email, 1)
                return
            else:
                print('ERRO! Escolha inválida')
            
def administrar_tarefas(email):
    while True:
        limpar_tela()
        tarefas = carregar_tarefas(email)
        print('='*40)
        print(f'{" TAREFAS ":^40}')
        print('='*40)
        print('[1] Criar Nova Tarefa\n'
              '[2] Editar Tarefa\n'
              '[3] Sair\n')
        tracinho()
        escolha = str(input('Selecione uma opção: ')).strip()
        if escolha == '1':
            while True:
                titulo = str(input('Informe o título da tarefa: ')).strip()
                if titulo == "":
                    print('ERRO! O título não pode ser vazio')
                    tracinho()
                else:
                    break
                
            while True:
                descricao = str(input('Informe os detalhes da tarefa: ')).strip()
                if descricao == "" or ' ' in descricao[0]:
                    print('ERRO! A descrição não pode ser vazia')
                    tracinho()
                else:
                    break

            while True:
                formato_padrao = r'\d{2}/\d{2}/\d{4}'
                data_prazo = input('Digite a data de vencimento (DD/MM/AAAA): ').strip()
                while not re.fullmatch(formato_padrao, data_prazo):
                    print ('Formato de data inválida!')
                    data_prazo = input('Digite a data de vencimento (DD/MM/AAAA): ').strip()
                try:
                    data_venc = datetime.strptime(data_prazo, '%d/%m/%Y')
                    hoje = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
                    if data_venc<hoje:
                        print('Data anterior a hoje não pode ser selecionada! Digite novamente')
                        continue
                    break
                except:
                    print('Data inexistente! Digite novamente')  

            while True:
                print('='*40)
                print(f'{" PRIORIDADES ":^40}')
                print('='*40)
                print('[1] Alta\n'
                    '[2] Média\n'
                    '[3] Baixa\n'
                    '[4] Sem prioridade\n')
                tracinho()
                escolha = str(input('Informe a prioridadea da tarefa: ')).strip()
                if escolha == '1':
                    prioridade = 'ALTA'
                    break
                elif escolha == '2':
                    prioridade = 'MEDIA'
                    break
                elif escolha == '3':
                    prioridade = 'BAIXA'
                    break
                elif escolha == '4':
                    prioridade = 'SEM PRIORIDADE'
                    break
                else:
                    print('ERRO! Informe um dígito válida')
                    tracinho()
                    break
            tarefas[email][prioridade].append({'Título': titulo, 'Descrição': descricao, 'Data': data_prazo, 'Prioridade': prioridade})
            with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
            tracinho()
            print('Tarefa adiciona com sucesso!')
            sleep(1)
            input('Clique na tecla "Enter" para voltar')
            from main import controle_pais
            controle_pais(email, 1)
            break
        elif escolha == '2':
            editar_tarefas(email)
            break
        elif escolha == '3':
            from main import controle_pais
            controle_pais(email, 1)
            break
        else:
            print('ERRO! Informe um dígito válida')
            tracinho()
        
    

                