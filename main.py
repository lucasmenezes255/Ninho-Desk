from cadastro import cadastrar_usuario, carregar_dados, redefinir_senha, email_valido, serie_valida, redefinir_senha_master
from util import tracinho, limpar_tela
from time import sleep
from tarefas import administrar_tarefas
from verificacoes import verifica_email, verifica_senha, verifica_senha_master
from lembretes import add_lembretes, ver_lembrete
from cronograma import ver_cronograma, organizar_cronograma
import maskpass
import json

def controle_pais(email, caminho):
    dados = carregar_dados()
    if caminho == 0:
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
                senha = maskpass.askpass(prompt='Informe a sua senha: ')
                verifica_senha_master(email, senha)
                break
            elif escolha == '2':
                redefinir_senha_master(email)
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
              '[5] Voltar para o Menu do Estudante')
        tracinho()
        escolha_menu = str(input('Selecione uma opção: \n'))

        if escolha_menu == '1':
            print('-'*40)
            novo_email = str(input('Digite seu novo email: '))
            novo_email = email_valido(novo_email)
            dados[novo_email] = dados[email]
            tracinho()
            with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                del dados[email]
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            print('Email redefinido com sucesso!')
            sleep(1)

        elif escolha_menu == '2':      
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
            email = email
            redefinir_senha(email)
            sleep(1)

        elif escolha_menu == '4':
            nova_serie = serie_valida()
            dados[email]['Série da Criança'] = nova_serie
            tracinho()
            with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            print('Série alterada com sucesso')
            sleep(1)

        elif escolha_menu == '5':
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
            conferir_tarefas()
            break
        elif escolha_menu == '2':       #Aqui pra redirecionar para as respectivas funções quando estiverem prontas
            ver_cronograma(email)
        elif escolha_menu == '3':
            ver_lembrete(email)
        elif escolha_menu == '4':
            print('FUNCIONALIDADE INDISPONÍVEL NO MOMENTO!')
            sleep(2)
        elif escolha_menu == '5':
            controle_pais(email, 0)
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
    limpar_tela()
    dados = carregar_dados()
    tracinho()
    print('Seja bem-vindo ao Ninho Desk🦉\nSeu APP de gerenciamento acadêmico!\nVamos iniciar?')
    tracinho()
    print('[1] Login')
    print('[2] Cadastrar novo usuário')
    print('[3] Sair')
    while True:
        try:
            tracinho()
            escolha = int(input('Escolha uma opção: '))
        except:
            print('Opção inválida! Tente novamente!')
        else:
            if escolha == 1:
                limpar_tela()
                tracinho()
                email = str(input('Informe o email de login: '))
                guia, email = verifica_email(email)
                if guia == 1:
                    login()
                    return
                elif guia == 2:
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
                            tracinho()
                            senha = maskpass.askpass(prompt='Informe a sua senha: ')
                            verifica_senha(email, senha)
                            break
                        elif escolha == 2:
                            tracinho()
                            redefinir_senha(email)
                            break
                        else:
                            print('Opção inválida! Tente novamente!')
                    break
            elif escolha == 2:
                limpar_tela()
                cadastrar_usuario()
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
                print('Opção inválida! Tente novamente!')

if __name__ == "__main__":
    login()

'''
 - Colocar código de verificação por email para quando for mudar a senha ou para quando tiver no esqueceu a senha
'''