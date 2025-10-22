from tarefas import carregar_tarefas
from datetime import datetime
from util import limpar_tela, tracinho
from time import sleep
from lembretes import ver_lembrete
import json
import os

def carregar_cronograma():
    if not os.path.exists('cronograma.json'):
        return {}
    with open('cronograma.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def salvar_cronograma(cronograma):
    with open('cronograma.json', 'w', encoding=  'utf-8') as arquivo:
        json.dump(cronograma, arquivo, indent=4, ensure_ascii=False)

def ver_cronograma(email):
    while True:
        limpar_tela()
        dados = carregar_tarefas(email)
        if email not in dados:
            tracinho()
            print('Nenhuma tarefa encontrada')
            tracinho()
            while True:
                tracinho()
                if input('\nTecle "ENTER" para voltar para o menu ') == "":
                    from main import menu_estudante
                    menu_estudante(email)
                    return
                else:
                    print('ERRO! Tecla errada')
                    tracinho()
        tarefas_usuario = dados[email]
        tarefas = (
            tarefas_usuario['Pendente']['ALTA']+
            tarefas_usuario['Pendente']['MEDIA']+
            tarefas_usuario['Pendente']['BAIXA']+
            tarefas_usuario['Pendente']['SEM PRIORIDADE']
        )
        tracinho()
        print('Cronograma de tarefas\n')
        if not tarefas:
            print('Nenhuma tarefa adicionada')
        tarefas_cronograma = sorted(
            tarefas, key=lambda tarefa:datetime.strptime(tarefa['Data'], '%d/%m/%Y')
        )
        for tarefa in tarefas_cronograma:
            print(f"{tarefa['Data']}: {tarefa['Título']}")
        tracinho()
        print('Cronograma de Estudos\n')
        cronograma = carregar_cronograma()
        if not email in cronograma:
            print('Nenhum cronograma de estudos adicionado')
            tracinho()
            while True:
                tracinho()
                if input('\nTecle "ENTER" para voltar para o menu ') == "":
                    from main import menu_estudante
                    menu_estudante(email)
                    return
                else:
                    print('ERRO! Tecla errada')
                    tracinho()
        else: 
            lista = cronograma[email]
            print(f"Segunda-Feira: {lista['Segunda-Feira']}\nTerça-Feira: {lista['Terça-Feira']}\nQuarta-Feira: {lista['Quarta-Feira']}\nQuinta-Feira: {lista['Quinta-Feira']}\nSexta-Feira: {lista['Sexta-Feira']}\nSábado: {lista['Sábado']}\nDomingo: {lista['Domingo']}")
            tracinho()
            print('[1] Adicionar algum lembrete\n[2] Sair\n')
            escolha = input('Selecione uma opção: ')
            if escolha == '1':
                limpar_tela()
                print('Direcionando')
                for i in range(3):
                    print('.')
                    sleep(1)
                ver_lembrete(email)
            elif escolha == '2':
                limpar_tela()
                print('Saindo')
                for i in range(3):
                    print('.')
                    sleep(1)
                limpar_tela()
                return
            else:
                tracinho()
                print ('Opção inválida! Tente novamente')
                sleep(1)

def organizar_cronograma(email):
    while True:
        limpar_tela()
        cronograma = carregar_cronograma()
        print('='*40)
        print(f'{" CRONOGRAMA ":^40}')
        print('='*40)
        print('[1] Ver Cronograma Existente\n'
              '[2] Adicionar Cronograma\n'
              '[3] Sair\n')
        tracinho()
        escolha = input('Selecione uma opção: ').strip()
        if escolha == '1':
            limpar_tela()
            tracinho()
            if email not in cronograma:
                cronograma[email] = {}
                print('Cronograma inexistente')
                sleep(1)
            else:
                lista = cronograma[email]
                print('Cronograma\n')
                print(f'Segunda-Feira: {lista["Segunda-Feira"]}\n Terça-Feira: {lista["Terça-Feira"]}\nQuarta-Feira: {lista["Quarta-Feira"]}\nQuinta-Feira: {lista["Quinta-Feira"]}\nSexta-Feira: {lista["Sexta-Feira"]}\nSábado: {lista["Sábado"]}\nDomingo: {lista["Domingo"]}')
                tracinho()
                while True:
                    tracinho()
                    if input('\nTecle "ENTER" para voltar para o menu ') == "":
                        organizar_cronograma(email)
                        return
                    else:
                        print('ERRO! Tecla errada')
                        tracinho()
        elif escolha == '2':
            add_cronograma(email)
        elif escolha == '3':
            limpar_tela()
            print('Saindo')
            for i in range(3):
                print('.')
                sleep(1)
            limpar_tela()
            return
        else:
            tracinho()
            print ('Opção inválida! Tente novamente')
            sleep(1)

def add_cronograma(email):
    limpar_tela()
    tracinho()
    print('Adicionando cronograma\n')
    segunda = input('Defina o que será estudado na Segunda-Feira: ')
    terca = input('Defina o que será estudado na Terça-Feira: ')
    quarta = input('Defina o que será estudado na Quarta-Feira: ')
    quinta = input('Defina o que será estudado na Quinta-Feira: ')
    sexta = input('Defina o que será estudado na Sexta-Feira: ')
    sabado = input('Defina o que será estudado no Sábado: ')
    domingo = input('Defina o que será estudado no Domingo: ')
    cronograma = carregar_cronograma()
    if email not in cronograma:
        cronograma[email] = []
    cronograma[email]= {"Segunda-Feira": segunda, "Terça-Feira": terca, "Quarta-Feira": quarta, "Quinta-Feira": quinta, "Sexta-Feira": sexta, "Sábado": sabado, "Domingo": domingo}
    salvar_cronograma(cronograma)
    tracinho()
    print('Cronograma adicionado com sucesso!')
    tracinho()
    while True:
        tracinho()
        if input('\nTecle "ENTER" para voltar para o menu ') == "":
            organizar_cronograma(email)
            return
        else:
            print('ERRO! Tecla errada')
            tracinho()
