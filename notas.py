from util import Util
import json
import os
from rich.table import Table
from rich import box
from rich.console import Console
import re

def carregar_notas(email):
    if not os.path.exists('notas.json'):
        notas = {email: {"PORTUGUES": {'Nota1': [0], 'Nota2': [0], 'Media': [0]}, 
                         "MATEMATICA": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                         "HISTORIA": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                         "GEOGRAFIA": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                         "CIENCIAS": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                         "EDUCACAOFISICA": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                         "ARTE": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                         "INGLES": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                         "ESPANHOL": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                         "FILOSOFIA": {'Nota1': [0], 'Nota2': [0], 'Media': [0]}}
                         }
        with open('notas.json', 'w', encoding='utf-8') as arq:
            json.dump(notas, arq, indent=4, ensure_ascii=False)
        return notas
    else:
        with open('notas.json', 'r', encoding='utf-8') as arq:
            notas = json.load(arq)
        if not email in notas:
            notas[email] = {"PORTUGUES": {'Nota1': [0], 'Nota2': [0], 'Media': [0]}, 
                            "MATEMATICA": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                            "HISTORIA": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                            "GEOGRAFIA": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                            "CIENCIAS": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                            "EDUCACAOFISICA": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                            "ARTE": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                            "INGLES": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                            "ESPANHOL": {'Nota1': [0], 'Nota2': [0], 'Media': [0]},
                            "FILOSOFIA": {'Nota1': [0], 'Nota2': [0], 'Media': [0]}
                            }
            with open('notas.json', 'w', encoding='utf-8') as arq:
                json.dump(notas, arq, indent=4, ensure_ascii=False)
            return notas
        return notas

class Notas:
    def __init__(self, email):
        self.email = email

    def exibir_tabela_notas(self):
        notas = carregar_notas(self.email)
        console = Console()
        # Criando as colunas da tabela de notas
        tabela_notas = Table(title='QUADRO DE NOTAS', show_lines=True)
        tabela_notas.add_column('Índice', justify='center')
        tabela_notas.add_column('Diciplina', justify='center')
        tabela_notas.add_column('Nota 1', justify='center')
        tabela_notas.add_column('Nota 2', justify='center')
        tabela_notas.add_column('Média', justify='center')
        # Criando as linhas da tabela de notas
        notas_email = notas[self.email]
        tabela_notas.add_row(str('1'), str('Português'), str(*notas_email['PORTUGUES']['Nota1']), 
                             str(*notas_email['PORTUGUES']['Nota2']), 
                             str(round((float(notas_email['PORTUGUES']['Nota1'][0]) + float(notas_email['PORTUGUES']['Nota2'][0]))/2, 1)))

        tabela_notas.add_row(str('2'), str('Matemática'), str(*notas_email['MATEMATICA']['Nota1']), 
                             str(*notas_email['MATEMATICA']['Nota2']), 
                             str(round((float(notas_email['MATEMATICA']['Nota1'][0]) + float(notas_email['MATEMATICA']['Nota2'][0]))/2, 1)))
        
        tabela_notas.add_row(str('3'), str('História'), str(*notas_email['HISTORIA']['Nota1']), 
                             str(*notas_email['HISTORIA']['Nota2']), 
                             str(round((float(notas_email['HISTORIA']['Nota1'][0]) + float(notas_email['HISTORIA']['Nota2'][0]))/2, 1)))
        
        tabela_notas.add_row(str('4'), str('Geografia'), str(*notas_email['GEOGRAFIA']['Nota1']), 
                             str(*notas_email['GEOGRAFIA']['Nota2']), 
                             str(round((float(notas_email['GEOGRAFIA']['Nota1'][0]) + float(notas_email['GEOGRAFIA']['Nota2'][0]))/2, 1)))
        
        tabela_notas.add_row(str('5'), str('Ciências'), str(*notas_email['CIENCIAS']['Nota1']), 
                             str(*notas_email['CIENCIAS']['Nota2']), 
                             str(round((float(notas_email['CIENCIAS']['Nota1'][0]) + float(notas_email['CIENCIAS']['Nota2'][0]))/2, 1)))
        
        tabela_notas.add_row(str('6'), str('Educação Física'), str(*notas_email['EDUCACAOFISICA']['Nota1']), 
                             str(*notas_email['EDUCACAOFISICA']['Nota2']), 
                             str(round((float(notas_email['EDUCACAOFISICA']['Nota1'][0]) + float(notas_email['EDUCACAOFISICA']['Nota2'][0]))/2, 1)))

        tabela_notas.add_row(str('7'), str('Arte'), str(*notas_email['ARTE']['Nota1']), 
                             str(*notas_email['ARTE']['Nota2']), 
                             str(round((float(notas_email['ARTE']['Nota1'][0]) + float(notas_email['ARTE']['Nota2'][0]))/2, 1)))
        
        tabela_notas.add_row(str('8'), str('Inglês'), str(*notas_email['INGLES']['Nota1']), 
                             str(*notas_email['INGLES']['Nota2']), 
                             str(round((float(notas_email['INGLES']['Nota1'][0]) + float(notas_email['INGLES']['Nota2'][0]))/2, 1)))
        
        tabela_notas.add_row(str('9'), str('Espanhol'), str(*notas_email['ESPANHOL']['Nota1']), 
                             str(*notas_email['ESPANHOL']['Nota2']), 
                             str(round((float(notas_email['ESPANHOL']['Nota1'][0]) + float(notas_email['ESPANHOL']['Nota2'][0]))/2, 1)))
        
        tabela_notas.add_row(str('10'), str('Filosofia'), str(*notas_email['FILOSOFIA']['Nota1']), 
                             str(*notas_email['FILOSOFIA']['Nota2']), 
                             str(round((float(notas_email['FILOSOFIA']['Nota1'][0]) + float(notas_email['FILOSOFIA']['Nota2'][0]))/2, 1)))
        
        console.print(tabela_notas)
    

    def exibir_notas_menu_estudante(self):
        self.exibir_tabela_notas()
        while True:
            Util.tracinho()
            escolha = str(input('Tecle "ENTER" para voltar para o menu'))
            if escolha == '':
                return
    def editar_notas(self):
        while True:
            Util.limpar_tela()
            self.exibir_tabela_notas()
            notas_completas = carregar_notas(self.email)
            notas_user = notas_completas[self.email]
            chaves_disciplinas = ['PORTUGUES', 'MATEMATICA', 'HISTORIA', 'GEOGRAFIA', 'CIENCIAS',
                                  'EDUCACAOFISICA', 'ARTE', 'INGLES', 'ESPANHOL', 'FILOSOFIA']
            while True:
                try:
                    disciplina = int(input('Informe o índice da disciplina que quer alterar: '))
                    if disciplina in [1,2,3,4,5,6,7,8,9,10]:
                        disciplina = chaves_disciplinas[disciplina - 1]
                        break
                    else:
                        print('\nERRO: Dígito inválido! Tente novamente')
                except:
                    print('\nERRO: Informe um dígito válido')
            Util.tracinho()
            while True:
                nota_editada = str(input('Informe a nota a ser editada (N1/N2): ')).strip().upper()
                if nota_editada == 'N1' or nota_editada == 'N2':
                    break
                else: 
                    print('\nERRO: Informe uma das opções de resposta corretamnte')
            Util.traco_igual()
            while True:
                nota = str(input('Informe a nova nota: '))
                if re.search(r'[a-zA-Z]', nota) or nota == '':
                    print('\nERRO: Informe um número')
                else:
                    break

            if ',' in nota:
                nota = nota.replace(',','.')
            nota = float(nota)
            if nota_editada == 'N1':
                notas_user[disciplina]['Nota1'].append(nota)
                del notas_user[disciplina]['Nota1'][0]

            elif nota_editada == 'N2':
                notas_user[disciplina]['Nota2'].append(nota)
                del notas_user[disciplina]['Nota2'][0]

            notas_completas[self.email] = notas_user
            with open('notas.json', 'w', encoding='utf-8') as arq:
                json.dump(notas_completas, arq, indent=4, ensure_ascii=False)

            while True:
                Util.tracinho()
                escolha = str(input('Tecle "ENTER" para voltar para o menu'))
                if escolha == '':
                    return