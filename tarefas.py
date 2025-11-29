from util import Util
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

class Tarefas:
    def __init__(self, email):
        self.email = email

    def conferir_tarefas(self):
        tarefas = carregar_tarefas(self.email)
        Util.limpar_tela()
        task = tarefas[self.email]
        for index, status in enumerate(task): 
                for indice, prioridade in enumerate(task[status]): 
                    for quant_task in range(0, len(task[status][prioridade])):
                        print(f'{index+1}.{indice+1} - Título: {task[status][prioridade][quant_task]["Título"]}\n   '
                            f'Descrição: {task[status][prioridade][quant_task]["Descrição"]}\n   ' \
                            f'Data: {task[status][prioridade][quant_task]["Data"]}\n   ' \
                            f'Prioridade: {task[status][prioridade][quant_task]["Prioridade"]}')
                        Util.tracinho()  
                        break
        print('='*40)
        print(f'{"LISTA DE TAREFAS":^40}')
        print('='*40)
        print('[1] Tarefas Pendentes\n'
            '[2] Tarefas Concluídas\n' 
            '[3] Sair')
        Util.tracinho()
        while True:
            escolha = str(input('Escolha uma opção: ')).strip()
            contador_tarefa = task['Pendente']
            if escolha == '1':
                Util.limpar_tela()
                if (len(contador_tarefa['ALTA'] + contador_tarefa['MEDIA'] + contador_tarefa['BAIXA'] + contador_tarefa['SEM PRIORIDADE'])) == 0:
                    Util.tracinho()
                    print('Sem tarefas disponíveis!')
                    Util.tracinho()
                else:
                    print('='*40)
                    print(f'{"TAREFAS PENDENTES":^40}')
                    print('='*40)
                    for indice, prioridade in enumerate(task["Pendente"]): 
                        for quant_task in range(0, len(task["Pendente"][prioridade])):
                            print(f'{indice+1}. Título: {task["Pendente"][prioridade][quant_task]["Título"]}\n   '
                                f'Descrição: {task["Pendente"][prioridade][quant_task]["Descrição"]}\n   ' 
                                f'Data: {task["Pendente"][prioridade][quant_task]["Data"]}\n   '
                                f'Prioridade: {task["Pendente"][prioridade][quant_task]["Prioridade"]}')
                            Util.tracinho()
                    while True:
                        escolha = str(input('Marcar uma tarefa como concluída [S/N]: ')).upper().strip()
                        if escolha == '' or escolha == ' ':
                            print('ERRO: Campo vazio! Tente novamente\n')
                            Util.tracinho()
                        elif not escolha in ['S', 'N']:
                            print('ERRO: Operação inválida! Tente novamente\n')
                            Util.tracinho()
                        else:
                            if escolha == 'S':
                                while True:
                                    titulo_tarefa = str(input('Informe o título da tarefa a ser concluída: ')).strip()
                                    if titulo_tarefa == '' or titulo_tarefa == ' ':
                                        print('ERRO: Campo vazio! Tente novamente\n')
                                        Util.tracinho()
                                    else:
                                        tarefa_inexistente = 0
                                        for indice, prioridade in enumerate(task["Pendente"]): 
                                            for quant_task in range(0, len(task["Pendente"][prioridade])):
                                                if titulo_tarefa == task["Pendente"][prioridade][quant_task]["Título"]:
                                                    tarefa_inexistente = 1
                                                    tarefa_copiada = tarefas[self.email]["Pendente"][prioridade][quant_task]
                                                    tarefas[self.email]['Concluída'][prioridade].append(tarefa_copiada)
                                                    del task["Pendente"][prioridade][quant_task]
                                                    with open('dados_tarefas.json', 'w', encoding='utf-8') as arq:
                                                        json.dump(tarefas, arq, indent=4, ensure_ascii=False)
                                                    print('\nMudança feita com sucesso!')
                                                    break
                                                
                                        if tarefa_inexistente == 0:
                                            print('ERRO: Tarefa inexistente! Tente novamente\n')
                                            Util.tracinho()
                                        else:
                                            break
                            elif escolha == 'N':
                                break
                break
            elif escolha == '2':
                contador_tarefa = task['Concluída']
                Util.limpar_tela()
                if (len(contador_tarefa['ALTA'] + contador_tarefa['MEDIA'] + contador_tarefa['BAIXA'] + contador_tarefa['SEM PRIORIDADE'])) == 0:
                    Util.tracinho()
                    print('Sem tarefas disponíveis!')
                    Util.tracinho()
                else:
                    print('='*40)
                    print(f'{"TAREFAS CONCLUÍDAS":^40}')
                    print('='*40)
                    for indice, prioridade in enumerate(task["Concluída"]): 
                        for quant_task in range(0, len(task["Concluída"][prioridade])):
                            print(f'{indice+1}. Título: {task["Concluída"][prioridade][quant_task]["Título"]}\n   '
                                f'Descrição: {task["Concluída"][prioridade][quant_task]["Descrição"]}\n   ' \
                                f'Data: {task["Concluída"][prioridade][quant_task]["Data"]}\n   ' \
                                f'Prioridade: {task["Concluída"][prioridade][quant_task]["Prioridade"]}')
                            Util.tracinho()  
                            break
                break
            elif escolha == '3':
                from main import menu_estudante
                menu_estudante(self.email)
                return
            else:
                print('ERRO! Informe um dígito válida')
                Util.tracinho()
        while True:
            Util.tracinho()
            if input('\nTecle "ENTER" para voltar para o menu ') == "":
                self.conferir_tarefas()
                break
            else:
                print('ERRO! Tecla errada')
                Util.tracinho()

    def administrar_tarefas(self):
        while True:
            Util.limpar_tela()
            tarefas = carregar_tarefas(self.email)
            print('='*40)
            print(f'{" TAREFAS ":^40}')
            print('='*40)
            print('[1] Criar Nova Tarefa\n'
                '[2] Editar Tarefa\n'
                '[3] Sair\n')
            Util.tracinho()

            escolha = str(input('Selecione uma opção: ')).strip()
            if escolha == '1':
                while True:
                    titulo = str(input('Informe o título da tarefa: ')).strip()
                    if titulo == "":
                        print('ERRO! O título não pode ser vazio')
                        Util.tracinho()
                    else:
                        break
                while True:
                    descricao = str(input('Informe os detalhes da tarefa: ')).strip()
                    if descricao == "" or ' ' in descricao[0]:
                        print('ERRO! A descrição não pode ser vazia')
                        Util.tracinho()
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
                    Util.tracinho()
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
                        Util.tracinho()
                tarefas[self.email]['Pendente'][prioridade].append({'Título': titulo, 'Descrição': descricao, 'Data': data_prazo, 'Prioridade': prioridade})
                with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                Util.tracinho()
                print('Tarefa adiciona com sucesso na aba Pendente!')
                sleep(1)
                while True:
                    if input('\nTecle "ENTER" para voltar para o menu ') == "":
                        self.administrar_tarefas()
                        break
                    else:
                        print('ERRO! Tecla errada')
                        Util.tracinho()
                from main import menu_controle_pais
                menu_controle_pais(self.email)
                break
            elif escolha == '2':
                self.editar_tarefas()
                break
            elif escolha == '3':
                from main import menu_controle_pais
                menu_controle_pais(self.email)
                break
            else:
                print('ERRO! Informe um dígito válida')
                Util.tracinho()

    def editar_tarefas(self):
        Util.limpar_tela()
        tarefas = carregar_tarefas(self.email)
        print('='*40)
        print(f'{"LISTA DE TAREFAS":^40}')
        print('='*40)
        Util.tracinho()
        task = tarefas[self.email]
        quantidade_task = len(task['Pendente']) + len(task['Concluída'])
        if quantidade_task == 0:
            print('')
            print('Sem tarefas!')
            sleep(1)
            self.administrar_tarefas(self.email)
            return
        else:
            for index, status in enumerate(task): 
                for indice, prioridade in enumerate(task[status]): 
                    for quant_task in range(0, len(task[status][prioridade])):
                        print(f'{index+1}.{indice+1} - Título: {task[status][prioridade][quant_task]["Título"]}\n   '
                            f'Descrição: {task[status][prioridade][quant_task]["Descrição"]}\n   ' 
                            f'Data: {task[status][prioridade][quant_task]["Data"]}\n   ' 
                            f'Prioridade: {task[status][prioridade][quant_task]["Prioridade"]}')
                        Util.tracinho()  
                        break
                        
            console = Console()
            tabela = Table(title='QUANTIDADE DE TAREFAS PENDENTES POR PRIORIDADE')
            tabela.add_column('Alta', style='red', justify='center')
            tabela.add_column('Média', style='yellow', justify='center')
            tabela.add_column('Baixa', style='green', justify='center')
            tabela.add_column('Sem Prioridade', style='black', justify='center')
            tabela.add_row(str(len(task['Pendente']["ALTA"])), 
                           str(len(task['Pendente']["MEDIA"])), 
                           str(len(task['Pendente']["BAIXA"])), 
                           str(len(task['Pendente']["SEM PRIORIDADE"])))
            console.print(tabela)

            console1 = Console()
            tabela1 = Table(title='QUANTIDADE DE TAREFAS CONCLUÍDAS POR PRIORIDADE')
            tabela1.add_column('Alta', style='red', justify='center')
            tabela1.add_column('Média', style='yellow', justify='center')
            tabela1.add_column('Baixa', style='green', justify='center')
            tabela1.add_column('Sem Prioridade', style='black', justify='center')
            tabela1.add_row(str(len(task['Concluída']["ALTA"])), 
                            str(len(task['Concluída']["MEDIA"])), 
                            str(len(task['Concluída']["BAIXA"])), 
                            str(len(task['Concluída']["SEM PRIORIDADE"])))
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
                                print(f'{indice+1}. Título: {task[status][prioridade][quant_task]["Título"]}\n   '
                                    f'Descrição: {task[status][prioridade][quant_task]["Descrição"]}\n   ' \
                                    f'Data: {task[status][prioridade][quant_task]["Data"]}\n   ' \
                                    f'Prioridade: {task[status][prioridade][quant_task]["Prioridade"]}')
                                Util.tracinho()  
                                if task[status][prioridade][quant_task]["Título"] == titulo_tarefa:
                                    tarefa_copiada = task[status][prioridade][quant_task]
                                    task[status][nova_prioridade].append(tarefa_copiada)
                                    del tarefas[self.email][status][prioridade][quant_task]
                    Util.tracinho()
                    print('Tarefa movida com sucesso!')
                    with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

                elif escolha == 2:
                    titulo_tarefa = str(input('Informe o título da tarefa que desejar apagar: '))
                    for index, status in enumerate(task): 
                        for indice, prioridade in enumerate(task[status]): 
                            for quant_task in range(0, len(task[status][prioridade])):
                                if task[status][prioridade][quant_task]["Título"] == titulo_tarefa:
                                    del tarefas[self.email][status][prioridade][quant_task]
                                    Util.tracinho()
                                    print('Tarefa apagada com sucesso!')
                                    break
                    with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                        
                elif escolha == 3:
                    while True:
                        titulo_tarefa = str(input('Informe o título da tarefa a ser concluída: ')).strip()
                        if titulo_tarefa == '' or titulo_tarefa == ' ':
                            print('ERRO: Campo vazio! Tente novamente\n')
                            Util.tracinho()
                        else:
                            tarefa_inexistente = 0
                            for index, status in enumerate(task): 
                                for indice, prioridade in enumerate(task[status]): 
                                    for quant_task in range(0, len(task[status][prioridade])):
                                        if titulo_tarefa == task[status][prioridade][quant_task]["Título"]:
                                            tarefa_inexistente = 1

                            if tarefa_inexistente == 0:
                                print('ERRO: Tarefa inexistente! Tente novamente\n')
                                Util.tracinho()
                            else:
                                break
                    Util.limpar_tela()
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
                                        Util.limpar_tela()
                                    elif escolha == 2:
                                        nova_descricao = str(input('Informe a nova descrição da tarefa: ')).strip()
                                        task[status][prioridade][quant_task]["Descrição"] = nova_descricao
                                        Util.limpar_tela()
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
                                        Util.limpar_tela()
                                    elif escolha == 4:
                                        Util.limpar_tela()
                                        self.editar_tarefas()
                                        break

                    Util.tracinho()
                    print('Tarefa movida com sucesso!')
                    with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                elif escolha == 4:
                    from main import menu_controle_pais
                    menu_controle_pais(self.email)
                    return
                else:
                    print('ERRO! Escolha inválida')