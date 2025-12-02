import json
import os
import re
import maskpass
from util import Util
from tarefas import carregar_tarefas
from lembretes import carregar_lembretes
from cronograma import carregar_cronograma
from notas import carregar_notas

def carregar_dados():
    # Em caso de não existir o arquivo, retorna um dicionário vazio
    if not os.path.exists('dados_usuarios.json'):
        return {}
    with open('dados_usuarios.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

class Usuario:
    def __init__(self, nome='', email='', serie='', senha='', senha_mestre='', confirma_senha='', confirma_senha_mestre=''):
        self.nome = nome
        self.email = email
        self.serie_crianca = serie
        self.__senha = senha
        self.__senha_mestre = senha_mestre
        self.__confirma_senha = confirma_senha
        self.__confirma_senha_mestre = confirma_senha_mestre

    def validar_nome(self):
        if len(self.nome) >= 30:
            return False
        if self.nome == '' or ' ' in self.nome[0]:
            return False
        elif self.nome[0] in '_-@!#%&*{[]}().':
            return False
        elif '@#$%&*({[]})' in self.nome:
            return False
        elif self.nome[0] in '0123456789':
            return False
        else:
            return True

    def validar_email(self):
        dados = carregar_dados()
        formato_padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if self.email in dados:
            return 1
        elif not re.fullmatch(formato_padrao, self.email):
            return 2
        else:
            return 3
                
    def cadastrar_senha(self):
        if self.__senha == '':
            return 0
        elif len(self.__senha) < 8:
            return 1
        else:
            if self.__confirma_senha != self.__senha:
                return 2
            else:
                return 3
                
    def cadastrar_senha_mestre(self):
        if self.__senha_mestre == '':
            return 0
        elif len(self.__senha_mestre) < 8:
            return 1
        elif not re.search('[a-zA-Z]', self.__senha_mestre):
            return 2
        elif not re.search('[0-9]', self.__senha_mestre):
            return 3
        else:
            if self.__confirma_senha_mestre != self.__senha_mestre:
                return 4
            else:
                return 5
        
    def validar_serie(self):
        try:
            self.serie_crianca = int(self.serie_crianca)
        except ValueError:
            return False
        if self.serie_crianca < 1 or self.serie_crianca > 9:
            return False
        else:
            return True
    
    def salvar_dados(self):
        # Carrega os dados existentes para dados_usuarios
        dados_usuarios = carregar_dados()
        dados_usuarios[self.email] = {'Nome': self.nome, 'Série da Criança': self.serie_crianca,'Senha': self.__senha, 'Senha Mestre': self.__senha_mestre}  # O email cadastrado é a chave dos dados novos
        with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados_usuarios, arquivo, indent=4, ensure_ascii=False)

    def redefinir_senha(self):
        if self.__senha == '':
            return 0
        elif len(self.__senha) < 8:
             return 1
        else:
            if self.__confirma_senha != self.__senha:
                return 3
            else:
                dados_usuarios = carregar_dados()
                dados_usuarios[self.email]['Senha'] = self.__senha
                with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(dados_usuarios, arquivo, indent=4, ensure_ascii=False)
        
    
    def redefinir_senha_master(self):
        while True:
            nova_senha = maskpass.askpass(prompt='Digite a senha mestre: ')
            if nova_senha == '':
                print('\nERRO: Senha não pode ser vazia!')
            elif len(nova_senha) < 8:
                print('\nERRO: Senha muito curta, deve ter pelo menos 8 caracteres')
                Util.tracinho()
            elif not re.search('[a-zA-Z]', nova_senha):
                print('\nERRO: A senha não possui letras')
                Util.tracinho()
            elif not re.search('[0-9]', nova_senha):
                print('\nERRO: A senha não possui números')
                Util.tracinho()
            else:
                confirmacao = maskpass.askpass(prompt='Confirme sua senha: ')
                if confirmacao != nova_senha:
                    print('\nERRO: Senha digitada não correspode, tente novamente')
                    Util.tracinho()
                else:
                    self.__senha_mestre = nova_senha
                    dados_usuarios = carregar_dados()
                    dados_usuarios[self.email]['Senha Mestre'] = self.__senha_mestre
                    with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(dados_usuarios, arquivo, indent=4, ensure_ascii=False)
                    break

    def mudar_email(self, novo_email):
        dados = carregar_dados()
        tarefas = carregar_tarefas(self.email)
        lembrete = carregar_lembretes()
        cronograma = carregar_cronograma()
        notas = carregar_notas(self.email)
        dados[novo_email] = {}
        dados[novo_email] = dados[self.email]
        del dados[self.email]
        with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        if self.email in tarefas:
            tarefas[novo_email] = tarefas[self.email]
            del tarefas[self.email]
            with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(tarefas, arquivo, indent=4,
                            ensure_ascii=False)

        if self.email in cronograma:
            cronograma[novo_email] = cronograma[self.email]
            del cronograma[self.email]
            with open('cronograma.json', 'w', encoding='utf-8') as arquivo:
                json.dump(cronograma, arquivo,
                            indent=4, ensure_ascii=False)

        if self.email in lembrete:
            lembrete[novo_email] = lembrete[self.email]
            del lembrete[self.email]
            with open('lembretes.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lembrete, arquivo, indent=4,
                            ensure_ascii=False)
                
        if self.email in notas:
            notas[novo_email] = notas[self.email]
            del notas[self.email]
            with open('notas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(notas, arquivo, indent=4,
                            ensure_ascii=False)
    
    def mudar_nome(self, novo_user):
        dados = carregar_dados()
        dados[self.email]['Nome'] = novo_user
        with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    
    def mudar_senha(self, nova_senha):
        dados = carregar_dados()
        dados[self.email]['Senha'] = nova_senha
        with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    
    def mudar_serie(self, nova_serie):
        dados = carregar_dados()
        dados[self.email]['Série da Criança'] = nova_serie
        with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                
    def apagar_perfil(self):
        dados = carregar_dados()
        tarefas = carregar_tarefas(self.email)
        lembrete = carregar_lembretes()
        cronograma = carregar_cronograma()
        notas = carregar_notas(self.email)
        if self.email in tarefas:
            del tarefas[self.email]
            with open('dados_tarefas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(tarefas, arquivo, indent=4,
                            ensure_ascii=False)
        if self.email in lembrete:
            del lembrete[self.email]
            with open('lembretes.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lembrete, arquivo, indent=4,
                            ensure_ascii=False)
        if self.email in cronograma:
            del cronograma[self.email]
            with open('cronograma.json', 'w', encoding='utf-8') as arquivo:
                json.dump(cronograma, arquivo,
                            indent=4, ensure_ascii=False)
        
        if self.email in notas:
            del notas[self.email]
            with open('notas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(notas, arquivo, indent=4,
                            ensure_ascii=False)
        if self.email in dados:
            del dados[self.email]
            with open('dados_usuarios.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        
    @staticmethod
    def verificando_serie(serie):
        while True:
            if serie < 1 or serie > 9:
                print('\nERRO: Série inválida!')
                Util.tracinho()
                try:
                    serie = int(input('Digite a série da criança: '))
                except:
                    print('\nERRO: Informe uma série válida!')
                    Util.tracinho()
            else:
                return serie
