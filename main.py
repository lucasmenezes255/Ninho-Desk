from cadastro import Usuario,carregar_dados
from util import tracinho, limpar_tela
from time import sleep
from tarefas import carregar_tarefas, Tarefas
from verificacoes import Verificacao
from lembretes import carregar_lembretes, Lembrete
from cronograma import carregar_cronograma, Cronograma
import json
import re

def controle_pais(email):
    verificando_senha = Verificacao(email)
    while True:
        limpar_tela()
        print('='*40)
        print(f'{"SENHA MESTRE":^40}')
        print('='*40)
        print('[1] Informe a senha\n'
                '[2] Esqueceu a senha\n')
        tracinho()
        escolha = str(input('Selecione uma opção: '))
        tracinho()
        if escolha == '1':
            verificando_senha.verificar_senha_master()
            break
        elif escolha == '2':
            verificando_senha.redefinir_senha_master()
    menu_controle_pais(email)
    return

def menu_controle_pais(email):
    while True:
        limpar_tela()
        print('='*40)
        print(f'{"CONTROLE DOS PAIS":^40}')
        print('='*40)
        print('[1] Administrar Tarefas\n'
              '[2] Organizar Cronograma\n'
              '[3] Criar Lembretes\n'
              '[4] Voltar para o Menu\n')
        tracinho()
        escolha_menu = str(input('Selecione uma opção: '))
        if escolha_menu == '1':
            tarefa = Tarefas(email)
            tarefa.administrar_tarefas()
            break
        elif escolha_menu == '2':       #Aqui pra redirecionar para as respectivas funções quando estiverem prontas
            cronograma = Cronograma(email)
            cronograma.organizar_cronograma()
            break
        elif escolha_menu == '3':
            lembrete = Lembrete(email)
            lembrete.add_lembretes()
        elif escolha_menu == '4':
            limpar_tela()
            print('Voltando')
            for i in range(3):
                print('.')
                sleep(1)
            from main import menu_estudante
            menu_estudante(email)
            break
        else:
            tracinho()
            print ('Opção inválida! Tente novamente')
            sleep(1)

class Edicao(Verificacao):
    def __init__(self, email, nome, serie):
        self.email = email
        self.nome = nome
        self.serie = serie
        
    def editar_perfil(self):    # Aqui o usuário pode alterar os dados do seu perfil
        while True:
            dados = carregar_dados()
            limpar_tela()
            print('='*40)
            print(f'{"MENU DE EDIÇÕES":^40}')
            print('='*40)
            print('[1] Editar Email\n'
                '[2] Editar Nome de Usuário\n'
                '[3] Editar Senha\n'
                '[4] Editar Série da Criança\n' 
                '[5] Apagar perfil\n' 
                '[6] Voltar para o Menu do Estudante')
            tracinho()
            escolha_menu = str(input('Selecione uma opção: \n'))

            if escolha_menu == '1':
                tarefas = carregar_tarefas(self.email)
                lembrete = carregar_lembretes()
                cronograma = carregar_cronograma()
                tracinho()
                novo_email = str(input('Digite seu novo email: '))
                novo_email = validar_email(novo_email)
                dados[novo_email] = dados[self.email]
                del dados[self.email]
                with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                if self.email in tarefas:
                    tarefas[novo_email] = tarefas[self.email]
                    del tarefas[self.email]
                    with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

                elif self.email in cronograma:
                    cronograma[novo_email] = cronograma[self.email]
                    del cronograma[self.email]
                    with open('cronograma.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(cronograma, arquivo, indent=4, ensure_ascii=False)

                elif self.email in lembrete:
                    lembrete[novo_email] = lembrete[self.email]
                    del lembrete[self.email]
                    with open('lembretes.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(lembrete, arquivo, indent=4, ensure_ascii=False)
                tracinho()
                sleep(1)
                self.editar_perfil()
                break
                
            elif escolha_menu == '2':
                tracinho()   
                while True:
                    novo_user = str(input('Digite seu novo nome: ')).strip()
                    if novo_user == '':
                        print('Nome não pode ser vazio!')
                        tracinho()
                    elif ' ' in novo_user[0]:
                        print('Nome não pode ser vazio!')
                        tracinho()
                    elif novo_user[0] in '0123456789':
                        print('Nome não pode ser começar com números!')
                        tracinho()
                    else:
                        break
                dados[self.email]['Nome'] = novo_user
                with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                print('Nome de usuário alterado com sucesso')
                sleep(1)

            elif escolha_menu == '3':
                tracinho()
                dados = carregar_dados()
                self.redefinir_senha()
                sleep(1)
                
            elif escolha_menu == '4':
                tracinho()
                dados = carregar_dados()
                nova_serie = self.cadastrar_serie()
                dados[self.email]['Série da Criança'] = nova_serie
                tracinho()
                with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                print('Série alterada com sucesso')
                sleep(1)

            elif escolha_menu == '5':
                tarefas = carregar_tarefas(self.email)
                lembrete = carregar_lembretes()
                cronograma = carregar_cronograma()
                tracinho()
                if self.email in tarefas:
                    del tarefas[self.email]
                    with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
                if self.email in lembrete:
                    del lembrete[self.email]
                    with open('lembretes.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(lembrete, arquivo, indent=4, ensure_ascii=False)
                if self.email in cronograma:
                    del cronograma[self.email]
                    with open('cronograma.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(cronograma, arquivo, indent=4, ensure_ascii=False)
                if self.email in dados:
                    del dados[self.email]
                    with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                tracinho()
                print('Apagando...\n')
                sleep(3)
                login()
                return
            elif escolha_menu == '6':
                limpar_tela()
                print('Voltando')
                for i in range(3):
                    print('.')
                    sleep(1)
                from main import menu_estudante
                menu_estudante(self.email)
                break
            else:
                tracinho()
                print ('\nERRO: Opção inválida! Tente novamente')
                sleep(1)
        
def validar_email(email):
    dados = carregar_dados()
    formato_padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        if email in dados:
            print('\nERRO: Email já cadastrado! Tente novamente')
            email = str(input('Digite seu email: '))
            tracinho()
        elif not re.fullmatch(formato_padrao, email):
                print('\nERRO: Email inválido!')
                tracinho()
                email = str(input('\nDigite seu email: '))
                tracinho()
        else:
            return email

def menu_estudante(email):
    while True:
        limpar_tela()
        print('='*40)
        print(f'{"MENU DO ESTUDANTE":^40}')
        print('='*40)
        print('[1] Conferir Tarefas\n'
            '[2] Ver Cronograma\n'
            '[3] Ver Lembretes\n'
            '[4] Pet Virtual\n'
            '[5] Controle dos Pais\n'
            '[6] Editar Perfil\n' \
            '[7] Sair')
        tracinho()
        escolha_menu = str(input('Selecione uma opção: '))
        if escolha_menu == '1':
            tarefa = Tarefas(email)
            tarefa.conferir_tarefas()
            break
        elif escolha_menu == '2':      #Aqui pra redirecionar para as respectivas funções quando estiverem prontas
            cronograma = Cronograma(email)
            cronograma.ver_cronograma()
            break
        elif escolha_menu == '3':
            lembrete = Lembrete(email)
            lembrete.ver_lembrete()
            break
        elif escolha_menu == '4':
            print('FUNCIONALIDADE INDISPONÍVEL NO MOMENTO!')
            sleep(2)
        elif escolha_menu == '5':
            controle_pais(email)
            break
        elif escolha_menu == '6':
            dado_usuario = carregar_dados()
            edita = dado_usuario[email]
            edita = Edicao(email, edita["Nome"], edita["Série da Criança"])
            edita.editar_perfil()
            break
        elif escolha_menu == '7':
            limpar_tela()
            print('Saindo')
            for i in range(3):
                print('.')
                sleep(1)
            limpar_tela()
            login()
            return
        else:
            tracinho()
            print ('Opção inválida! Tente novamente')
            sleep(1)
    
def login():
    while True:
        limpar_tela()
        tracinho()
        print('Seja bem-vindo ao Ninho Desk🦉\n'
              'Seu APP de gerenciamento acadêmico!\n'
              'Vamos iniciar?')
        tracinho()
        print('[1] Login')
        print('[2] Cadastrar novo usuário')
        print('[3] Sair')
        try:
            tracinho()
            escolha = int(input('Escolha uma opção: '))
        except:
            print('\nERRO: Opção inválida! Tente novamente!')
            tracinho()
            sleep(1)
        else:
            if escolha == 1:
                limpar_tela()
                tracinho()
                email = str(input('Informe o email de login: '))
                validacao = Verificacao(email)
                validacao.verifica_email_login()
                while True:
                    tracinho()
                    print('[1] Informe a senha')
                    print('[2] Esqueceu a senha')
                    while True:
                        try:
                            tracinho()
                            escolha = int(input('Escolha uma opção acima: '))
                        except:
                            print('Opção inválida! Tente novamente!')
                        else:
                            break
                    if escolha == 1:
                        validacao.verificar_senha()
                        menu_estudante(validacao.email)
                        return
                    elif escolha == 2:
                        tracinho()
                        validacao.redefinir_senha()
                        menu_estudante(validacao.email)
                        return
                    else:
                        print('Opção inválida! Tente novamente!')
            elif escolha == 2:
                limpar_tela()
                usuario = Usuario()
                usuario.validar_username()
                login()
                break
            elif escolha == 3:
                limpar_tela()
                tracinho()
                print('Nos despedimos por aqui, até a próxima!')
                sleep(1)
                for i in range(3):
                    print('.')
                    sleep(1)
                tracinho()
                print('Ninho Desk🦉')
                tracinho()
                return
            else:
                print('\nERRO: Opção inválida! Tente novamente!')
                tracinho()
                sleep(1)

if __name__ == "__main__":
    login()
