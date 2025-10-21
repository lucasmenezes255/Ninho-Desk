from util import limpar_tela, tracinho
from time import sleep
import json
import os

def carregar_lembretes():
    if not os.path.exists('lembretes.json'):
        return {}
    with open('lembretes.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def salvar_lembretes(lembretes):
    with open('lembretes.json', 'w', encoding=  'utf-8') as arquivo:
        json.dump(lembretes, arquivo, indent=4, ensure_ascii=False)

def add_lembretes(email):
    tit_lembrete = input('Digite o título do lembrete a ser adicionado: ')
    desc_lembrete = input('Digite a descrição do lembrete: ')
    lembretes = carregar_lembretes()
    if email not in lembretes:
        lembretes[email] = []
    lembretes[email].append({'Título': tit_lembrete, 'Descrição': desc_lembrete})
    salvar_lembretes(lembretes)
    print('Lembrete adicionado com sucesso!')

def lista_lembretes(email):
    lembretes = carregar_lembretes()
    if email not in lembretes or len(lembretes)==0:
        limpar_tela()
        tracinho()
        print('Nenhum lembrete definido!')
        tracinho()
        input('Clique na tecla "Enter" para voltar')
    elif len(lembretes) >= 1:
        tracinho()
        print('Seus lembretes:')
        for i, lembrete in enumerate (lembretes[email], start=1):
            print(f'\n {[i]} {lembrete['Título']}:\n{lembrete['Descrição']}')
        tracinho()
        input('Clique na tecla "Enter" para voltar')

def ver_lembrete(email):
    while True:
            limpar_tela()
            tracinho()
            print('[1] Acessar lista de lembretes\n[2] Adicionar lembretes\n[3] Voltar ao Menu do Estudante')
            tracinho()
            escolha = input('Selecione uma opção: ')
            if escolha == '1':
                lista_lembretes(email)
            elif escolha == '2':
                add_lembretes(email)
            elif escolha == '3':
                limpar_tela()
                print('Saindo')
                for i in range(3):
                    print('.')
                    sleep(1)
                limpar_tela()
                from main import menu_estudante
                menu_estudante(email)
                break
            else:
                tracinho()
                print ('Opção inválida! Tente novamente')
                sleep(1)