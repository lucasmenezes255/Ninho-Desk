from tarefas import carregar_tarefas
from datetime import datetime
from util import limpar_tela, tracinho
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

    def ver_cronograma(self):
        while True:
            limpar_tela()
            dados = carregar_tarefas(self.email)
            if self.email not in dados:
                tracinho()
                print('Nenhuma tarefa encontrada')
                tracinho()
                while True:
                    tracinho()
                    if input('\nTecle "ENTER" para voltar para o menu ') == "":
                        from main import menu_estudante
                        menu_estudante(self.email)
                        return
                    else:
                        print('ERRO! Tecla errada')
                        tracinho()
            tarefas_usuario = dados[self.email]
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
            if not self.email in cronograma:
                print('Nenhum cronograma de estudos adicionado')
                tracinho()
                while True:
                    tracinho()
                    if input('\nTecle "ENTER" para voltar para o menu ') == "":
                        from main import menu_estudante
                        menu_estudante(self.email)
                        return
                    else:
                        print('ERRO! Tecla errada')
                        tracinho()
            else: 
                lista = cronograma[self.email]
                print(f"Segunda-Feira: {lista['Segunda-Feira']}\n"
                    f"Terça-Feira: {lista['Terça-Feira']}\n" \
                    f"Quarta-Feira: {lista['Quarta-Feira']}\n" \
                    f"Quinta-Feira: {lista['Quinta-Feira']}\n" \
                    f"Sexta-Feira: {lista['Sexta-Feira']}\n" \
                    f"Sábado: {lista['Sábado']}\n" \
                    f"Domingo: {lista['Domingo']}")
                tracinho()
                print('[1] Lembretes\n[2] Sair\n')
                escolha = input('Selecione uma opção: ')
                if escolha == '1':
                    limpar_tela()
                    print('Direcionando')
                    for i in range(3):
                        print('.')
                        sleep(1)
                    self.ver_lembrete()
                    return
                elif escolha == '2':
                    limpar_tela()
                    from  main import menu_estudante
                    menu_estudante(self.email)
                    return
                else:
                    tracinho()
                    print ('Opção inválida! Tente novamente')
                    sleep(1)

    def organizar_cronograma(self):
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
                if self.email not in cronograma:
                    cronograma[self.email] = {}
                    print('Cronograma inexistente')
                    sleep(1)
                else:
                    lista = cronograma[self.email]
                    print('Cronograma\n')
                    print(f'Segunda-Feira: {lista["Segunda-Feira"]}\n'
                        f'Terça-Feira: {lista["Terça-Feira"]}\n' \
                        f'Quarta-Feira: {lista["Quarta-Feira"]}\n' \
                        f'Quinta-Feira: {lista["Quinta-Feira"]}\n' \
                        f'Sexta-Feira: {lista["Sexta-Feira"]}\n' \
                        f'Sábado: {lista["Sábado"]}\n' \
                        f'Domingo: {lista["Domingo"]}')
                    tracinho()
                    while True:
                        tracinho()
                        if input('\nTecle "ENTER" para voltar para o menu ') == "":
                            self.organizar_cronograma()
                            return
                        else:
                            print('ERRO! Tecla errada')
                            tracinho()
            elif escolha == '2':
                self.add_cronograma()
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

    def add_cronograma(self):
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
        tracinho()
        print('Cronograma adicionado com sucesso!')
        tracinho()
        while True:
            tracinho()
            if input('\nTecle "ENTER" para voltar para o menu ') == "":
                self.organizar_cronograma()
                return
            else:
                print('ERRO! Tecla errada')
                tracinho()

    @staticmethod
    def salvar_cronograma(cronograma):
        with open('cronograma.json', 'w', encoding=  'utf-8') as arquivo:
            json.dump(cronograma, arquivo, indent=4, ensure_ascii=False)