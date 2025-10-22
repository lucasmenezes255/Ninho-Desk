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
    
def conferir_tarefas(email):
    tarefas = carregar_tarefas(email)
    limpar_tela()
    task = tarefas[email]
    for index, status in enumerate(task): 
            for indice, prioridade in enumerate(task[status]): 
                for quant_task in range(0, len(task[status][prioridade])):
                    print(f'{index+1}.{indice+1} - Título: {task[status][prioridade][quant_task]["Título"]}\n   Descrição: {task[status][prioridade][quant_task]["Descrição"]}\n   Data: {task[status][prioridade][quant_task]["Data"]}\n   Prioridade: {task[status][prioridade][quant_task]["Prioridade"]}')
                    tracinho()  
                    break
    print('='*40)
    print(f'{"LISTA DE TAREFAS":^40}')
    print('='*40)
    print('[1] Tarefas Pendentes\n'
          '[2] Tarefas Concluídas\n' 
          '[3] Sair')
    tracinho()
    while True:
        escolha = str(input('Escolha uma opção: ')).strip()
        contador_tarefa = task['Pendente']
        if escolha == '1':
            limpar_tela()
            if (len(contador_tarefa['ALTA'] + contador_tarefa['MEDIA'] + contador_tarefa['BAIXA'] + contador_tarefa['SEM PRIORIDADE'])) == 0:
                tracinho()
                print('Sem tarefas disponíveis!')
                tracinho()
            else:
                print('='*40)
                print(f'{"TAREFAS PENDENTES":^40}')
                print('='*40)
                for indice, prioridade in enumerate(task["Pendente"]): 
                    for quant_task in range(0, len(task["Pendente"][prioridade])):
                        print(f'{indice+1}. Título: {task["Pendente"][prioridade][quant_task]["Título"]}\n   Descrição: {task["Pendente"][prioridade][quant_task]["Descrição"]}\n   Data: {task["Pendente"][prioridade][quant_task]["Data"]}\n   Prioridade: {task["Pendente"][prioridade][quant_task]["Prioridade"]}')
                        tracinho()
                while True:
                    escolha = str(input('Marcar uma tarefa como concluída [S/N]: ')).upper().strip()
                    if escolha == '' or escolha == ' ':
                        print('ERRO: Campo vazio! Tente novamente\n')
                        tracinho()
                    elif not escolha in ['S', 'N']:
                        print('ERRO: Operação inválida! Tente novamente\n')
                        tracinho()
                    else:
                        if escolha == 'S':
                            while True:
                                titulo_tarefa = str(input('Informe o título da tarefa a ser concluída: ')).strip()
                                if titulo_tarefa == '' or titulo_tarefa == ' ':
                                    print('ERRO: Campo vazio! Tente novamente\n')
                                    tracinho()
                                else:
                                    tarefa_inexistente = 0
                                    for indice, prioridade in enumerate(task["Pendente"]): 
                                        for quant_task in range(0, len(task["Pendente"][prioridade])):
                                            if titulo_tarefa == task["Pendente"][prioridade][quant_task]["Título"]:
                                                tarefa_inexistente = 1
                                                tarefa_copiada = tarefas[email]["Pendente"][prioridade][quant_task]
                                                tarefas[email]['Concluída'][prioridade].append(tarefa_copiada)
                                                del task["Pendente"][prioridade][quant_task]
                                                with open('dados_tarefas.json', 'w', encoding='utf-8') as arq:
                                                    json.dump(tarefas, arq, indent=4, ensure_ascii=False)
                                                print('\nMudança feita com sucesso!')
                                                break
                                            
                                    if tarefa_inexistente == 0:
                                        print('ERRO: Tarefa inexistente! Tente novamente\n')
                                        tracinho()
                                    else:
                                        break
                        elif escolha == 'N':
                            break
            break
        elif escolha == '2':
            contador_tarefa = task['Concluída']
            limpar_tela()
            if (len(contador_tarefa['ALTA'] + contador_tarefa['MEDIA'] + contador_tarefa['BAIXA'] + contador_tarefa['SEM PRIORIDADE'])) == 0:
                tracinho()
                print('Sem tarefas disponíveis!')
                tracinho()
            else:
                print('='*40)
                print(f'{"TAREFAS CONCLUÍDAS":^40}')
                print('='*40)
                for indice, prioridade in enumerate(task["Concluída"]): 
                    for quant_task in range(0, len(task["Concluída"][prioridade])):
                        print(f'{indice+1}. Título: {task["Concluída"][prioridade][quant_task]["Título"]}\n   Descrição: {task["Concluída"][prioridade][quant_task]["Descrição"]}\n   Data: {task["Concluída"][prioridade][quant_task]["Data"]}\n   Prioridade: {task["Concluída"][prioridade][quant_task]["Prioridade"]}')
                        tracinho()  
                        break
            break
        elif escolha == '3':
            from main import menu_estudante
            menu_estudante(email)
            return
        else:
            print('ERRO! Informe um dígito válida')
            tracinho()
    while True:
        tracinho()
        if input('\nTecle "ENTER" para voltar para o menu ') == "":
            conferir_tarefas(email)
            break
        else:
            print('ERRO! Tecla errada')
            tracinho()
    
def editar_tarefas(email):
    limpar_tela()
    tarefas = carregar_tarefas(email)
    print('='*40)
    print(f'{"LISTA DE TAREFAS":^40}')
    print('='*40)
    tracinho()
    task = tarefas[email]
    quantidade_task = len(task['Pendente']) + len(task['Concluída'])
    if quantidade_task == 0:
        print('')
        print('Sem tarefas!')
        sleep(1)
        administrar_tarefas(email)
        return
    else:
        for index, status in enumerate(task): 
            for indice, prioridade in enumerate(task[status]): 
                for quant_task in range(0, len(task[status][prioridade])):
                    print(f'{index+1}.{indice+1} - Título: {task[status][prioridade][quant_task]["Título"]}\n   Descrição: {task[status][prioridade][quant_task]["Descrição"]}\n   Data: {task[status][prioridade][quant_task]["Data"]}\n   Prioridade: {task[status][prioridade][quant_task]["Prioridade"]}')
                    tracinho()  
                    break
                    
        console = Console()
        tabela = Table(title='QUANTIDADE DE TAREFAS PENDENTES POR PRIORIDADE')
        tabela.add_column('Alta', style='red', justify='center')
        tabela.add_column('Média', style='yellow', justify='center')
        tabela.add_column('Baixa', style='green', justify='center')
        tabela.add_column('Sem Prioridade', style='black', justify='center')
        tabela.add_row(str(len(task['Pendente']["ALTA"])), str(len(task['Pendente']["MEDIA"])), str(len(task['Pendente']["BAIXA"])), str(len(task['Pendente']["SEM PRIORIDADE"])))
        console.print(tabela)

        console1 = Console()
        tabela1 = Table(title='QUANTIDADE DE TAREFAS CONCLUÍDAS POR PRIORIDADE')
        tabela1.add_column('Alta', style='red', justify='center')
        tabela1.add_column('Média', style='yellow', justify='center')
        tabela1.add_column('Baixa', style='green', justify='center')
        tabela1.add_column('Sem Prioridade', style='black', justify='center')
        tabela1.add_row(str(len(task['Concluída']["ALTA"])), str(len(task['Concluída']["MEDIA"])), str(len(task['Concluída']["BAIXA"])), str(len(task['Concluída']["SEM PRIORIDADE"])))
        console1.print(tabela1)

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
                titulo_tarefa = str(input('Informe o título da tarefa que desejar mover: ')).strip()
                nova_prioridade = str(input('Informe a nova prioridade da tarefa: ')).strip().upper()
                for index, status in enumerate(task): 
                    for indice, prioridade in enumerate(task[status]): 
                        for quant_task in range(0, len(task[status][prioridade])):
                            print(f'{indice+1}. Título: {task[status][prioridade][quant_task]["Título"]}\n   Descrição: {task[status][prioridade][quant_task]["Descrição"]}\n   Data: {task[status][prioridade][quant_task]["Data"]}\n   Prioridade: {task[status][prioridade][quant_task]["Prioridade"]}')
                            tracinho()  
                            if task[status][prioridade][quant_task]["Título"] == titulo_tarefa:
                                tarefa_copiada = task[status][prioridade][quant_task]
                                task[status][nova_prioridade].append(tarefa_copiada)
                                del tarefas[email][status][prioridade][quant_task]
                tracinho()
                print('Tarefa movida com sucesso!')
                with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

            elif escolha == 2:
                titulo_tarefa = str(input('Informe o título da tarefa que desejar apagar: '))
                for index, status in enumerate(task): 
                    for indice, prioridade in enumerate(task[status]): 
                        for quant_task in range(0, len(task[status][prioridade])):
                            if task[status][prioridade][quant_task]["Título"] == titulo_tarefa:
                                del tarefas[email][status][prioridade][quant_task]
                                tracinho()
                                print('Tarefa apagada com sucesso!')
                                break
                with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                    
            elif escolha == 3:
                while True:
                    titulo_tarefa = str(input('Informe o título da tarefa a ser concluída: ')).strip()
                    if titulo_tarefa == '' or titulo_tarefa == ' ':
                        print('ERRO: Campo vazio! Tente novamente\n')
                        tracinho()
                    else:
                        tarefa_inexistente = 0
                        for index, status in enumerate(task): 
                            for indice, prioridade in enumerate(task[status]): 
                                for quant_task in range(0, len(task[status][prioridade])):
                                    if titulo_tarefa == task["Pendente"][prioridade][quant_task]["Título"]:
                                        tarefa_inexistente = 1

                        if tarefa_inexistente == 0:
                            print('ERRO: Tarefa inexistente! Tente novamente\n')
                            tracinho()
                        else:
                            break
                print('='*40)
                print(f'{"MENU DE EDIÇÕES":^40}')
                print('='*40)
                print('[1] Editar Título\n'
                      '[2] Editar Descrição\n' 
                      '[3] Editar Prazo\n' 
                      '[4] Sair ')
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
                for index, status in enumerate(task): 
                    for indice, prioridade in enumerate(task[status]): 
                        for quant_task in range(0, len(task[status][prioridade])):
                            if task[status][prioridade][quant_task]["Título"] == titulo_tarefa:
                                if escolha == 1:
                                    novo_titulo = str(input('Informe o novo título: ')).strip()
                                    task[status][prioridade][quant_task]["Título"] = novo_titulo
                                    limpar_tela()
                                elif escolha == 2:
                                    nova_descricao = str(input('Informe a nova descrição da tarefa: ')).strip()
                                    task[status][prioridade][quant_task]["Descrição"] = nova_descricao
                                    limpar_tela()
                                elif escolha == 3:
                                    while True:
                                        formato_padrao = r'\d{2}/\d{2}/\d{4}'
                                        novo_prazo = input('Digite a data de vencimento (DD/MM/AAAA): ').strip()
                                        while not re.fullmatch(formato_padrao, novo_prazo):
                                            print ('ERRO: Formato de data inválida!\n')
                                            novo_prazo = input('Digite a data de vencimento (DD/MM/AAAA): ').strip()
                                        try:
                                            data_venc = datetime.strptime(novo_prazo, '%d/%m/%Y')
                                            hoje = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
                                            if data_venc<hoje:
                                                print('\nERRO: Data anterior a hoje não pode ser selecionada! Digite novamente')
                                                continue
                                            break
                                        except:
                                            print('\nERRO: Data inexistente! Digite novamente')
                                    
                                    task[status][prioridade][quant_task]["Data"] = novo_prazo
                                    limpar_tela()
                                elif escolha == 4:
                                    limpar_tela()
                                    editar_tarefas()
                                    break

                tracinho()
                print('Tarefa movida com sucesso!')
                with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
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
                    print ('\nERRO: Formato de data inválida!')
                    data_prazo = input('Digite a data de vencimento (DD/MM/AAAA): ').strip()
                try:
                    data_venc = datetime.strptime(data_prazo, '%d/%m/%Y')
                    hoje = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
                    if data_venc<hoje:
                        print('\nERRO: Data anterior a hoje não pode ser selecionada! Digite novamente')
                        continue
                    break
                except:
                    print('\nERRO: Data inexistente! Digite novamente')  

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
            tarefas[email]['Pendente'][prioridade].append({'Título': titulo, 'Descrição': descricao, 'Data': data_prazo, 'Prioridade': prioridade})
            with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
            tracinho()
            print('Tarefa adiciona com sucesso na aba Pendente!')
            sleep(1)
            while True:
                if input('\nTecle "ENTER" para voltar para o menu ') == "":
                    administrar_tarefas(email)
                    break
                else:
                    print('ERRO! Tecla errada')
                    tracinho()
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