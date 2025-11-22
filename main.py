from cadastro import Usuario
from cadastro import carregar_dados
from util import tracinho, limpar_tela, traco_igual
from time import sleep
from tarefas import administrar_tarefas, conferir_tarefas, carregar_tarefas

from verificacoes import Verificacao
from lembretes import add_lembretes, ver_lembrete, carregar_lembretes
from cronograma import ver_cronograma, organizar_cronograma, carregar_cronograma
import maskpass
import json

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
            administrar_tarefas(email)
            break
        elif escolha_menu == '2':       #Aqui pra redirecionar para as respectivas funções quando estiverem prontas
            organizar_cronograma(email)
        elif escolha_menu == '3':
            add_lembretes(email)
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

def editar_perfil(email):    # Aqui o usuário pode alterar os dados do seu perfil
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
            tarefas = carregar_tarefas(email)
            lembrete = carregar_lembretes()
            cronograma = carregar_cronograma(email)
            tracinho()
            novo_email = str(input('Digite seu novo email: '))
            novo_email = email_valido(novo_email)
            dados[novo_email] = dados[email]
            tarefas[novo_email] = tarefas[email]
            lembrete[novo_email] = lembrete[email]
            cronograma[novo_email] = cronograma[email]
            tracinho()
            with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                del dados[email]
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)

            with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                del tarefas[email]
                json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

            with open('lembretes.json', 'w', encoding='utf-8') as arquivo:
                del lembrete[email]
                json.dump(lembrete, arquivo, indent=4, ensure_ascii=False)

            with open('cronograma.json', 'w', encoding='utf-8') as arquivo:
                del cronograma[email]
                json.dump(cronograma, arquivo, indent=4, ensure_ascii=False)
            print('Email redefinido com sucesso!')
            sleep(1)
            editar_perfil(novo_email)
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
            dados[email]['Nome'] = novo_user
            with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            print('Nome de usuário alterado com sucesso')
            sleep(1)

        elif escolha_menu == '3':
            tracinho()
            dados = carregar_dados()
            email = email
            redefinir_senha(email)
            sleep(1)

        elif escolha_menu == '4':
            tracinho()
            dados = carregar_dados()
            nova_serie = serie_valida()
            dados[email]['Série da Criança'] = nova_serie
            tracinho()
            with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            print('Série alterada com sucesso')
            sleep(1)

        elif escolha_menu == '5':
            tracinho()
            dados = carregar_dados()
            tarefas = carregar_tarefas(email)
            lembrete = carregar_lembretes()
            cronograma = carregar_cronograma()

            with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                del dados[email]
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            
            with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                del tarefas[email]
                json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

            with open('lembretes.json', 'w', encoding='utf-8') as arquivo:
                del lembrete[email]
                json.dump(lembrete, arquivo, indent=4, ensure_ascii=False)

            with open('cronograma.json', 'w', encoding='utf-8') as arquivo:
                del cronograma[email]
                json.dump(cronograma, arquivo, indent=4, ensure_ascii=False)
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
            menu_estudante(email)
            break
        else:
            tracinho()
            print ('\nERRO: Opção inválida! Tente novamente')
            sleep(1)

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
            conferir_tarefas(email)
            break
        elif escolha_menu == '2':       #Aqui pra redirecionar para as respectivas funções quando estiverem prontas
            ver_cronograma(email)
        elif escolha_menu == '3':
            ver_lembrete(email)
        elif escolha_menu == '4':
            print('FUNCIONALIDADE INDISPONÍVEL NO MOMENTO!')
            sleep(2)
        elif escolha_menu == '5':
            controle_pais(email)
            break
        elif escolha_menu == '6':
            editar_perfil(email)
            break
        elif escolha_menu == '7':
            limpar_tela()
            print('Saindo')
            for i in range(3):
                print('.')
                sleep(1)
            limpar_tela()
            login()
            break
        else:
            tracinho()
            print ('Opção inválida! Tente novamente')
            sleep(1)
    
def login():
    while True:
        limpar_tela()
        dados = carregar_dados()
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
                break
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
                break
            else:
                print('\nERRO: Opção inválida! Tente novamente!')
                tracinho()
                sleep(1)

if __name__ == "__main__":
    login()
