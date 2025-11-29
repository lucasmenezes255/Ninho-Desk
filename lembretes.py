from util import Util
from time import sleep
import json
import os

def carregar_lembretes():
    if not os.path.exists('lembretes.json'):
        return {}
    with open('lembretes.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

class Lembrete:
    def __init__(self, email):
        self.email = email

    def ver_lembrete(self):
        while True:
            Util.limpar_tela()
            Util.tracinho()
            print('[1] Acessar lista de lembretes\n'
                '[2] Adicionar lembretes\n'
                '[3] Voltar ao Menu do Estudante')
            Util.tracinho()
            escolha = input('Selecione uma opção: ')
            if escolha == '1':
                self.lista_lembretes()
                break
            elif escolha == '2':
                self.add_lembretes()
                sleep(1)
            elif escolha == '3':
                Util.limpar_tela()
                print('Saindo')
                for i in range(3):
                    print('.')
                    sleep(1)
                Util.limpar_tela()
                from main import menu_estudante
                menu_estudante(self.email)
                return
            else:
                Util.tracinho()
                print ('Opção inválida! Tente novamente')
                sleep(1)


    def add_lembretes(self):
        while True:
            tit_lembrete = input('Digite o título do lembrete a ser adicionado: ').strip()
            Util.tracinho()
            if tit_lembrete == '' or  ' ' in tit_lembrete[0]:
                print('\nERRO: Título não pode ser vazio!')
            else:
                break
        while True:
            desc_lembrete = input('Digite a descrição do lembrete: ').strip()
            Util.tracinho()
            if desc_lembrete == '' or  ' ' in desc_lembrete[0]:
                print('\nERRO: Descrição não pode ser vazio!')
            else:
                break
        lembretes = carregar_lembretes()
        if self.email not in lembretes:
            lembretes[self.email] = []
        lembretes[self.email].append({'Título': tit_lembrete, 'Descrição': desc_lembrete})
        self.salvar_lembretes(lembretes)
        print('Lembrete adicionado com sucesso!')
    
    @staticmethod
    def salvar_lembretes(lembretes):
        with open('lembretes.json', 'w', encoding=  'utf-8') as arquivo:
            json.dump(lembretes, arquivo, indent=4, ensure_ascii=False)

    def lista_lembretes(self):
        lembretes = carregar_lembretes()
        if self.email not in lembretes or len(lembretes)==0:
            Util.limpar_tela()
            Util.tracinho()
            print('Nenhum lembrete definido!')
            while True:
                Util.tracinho()
                if input('\nTecle "ENTER" para voltar para o menu ') == "":
                    self.ver_lembrete()
                    break
                else:
                    print('ERRO! Tecla errada')
                    Util.tracinho()
        elif len(lembretes) >= 1:
            Util.tracinho()
            print('Seus lembretes:')
            for i, lembrete in enumerate (lembretes[self.email], start=1):
                print(f'\n {[i]} {lembrete["Título"]}:\n{lembrete["Descrição"]}')
            while True:
                Util.tracinho()
                if input('\nTecle "ENTER" para voltar para o menu ') == "":
                    self.ver_lembrete()
                    break
                else:
                    print('ERRO! Tecla errada')
                    Util.tracinho()