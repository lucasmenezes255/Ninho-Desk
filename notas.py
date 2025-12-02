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

    def editar_nota1(self, nota, indice,):
        notas_completas = carregar_notas(self.email)
        notas_user = notas_completas[self.email]
        chaves_disciplinas = ['PORTUGUES', 'MATEMATICA', 'HISTORIA', 'GEOGRAFIA', 'CIENCIAS',
                                'EDUCACAOFISICA', 'ARTE', 'INGLES', 'ESPANHOL', 'FILOSOFIA']
        indice = int(indice)
        indice = chaves_disciplinas[indice - 1]
        if nota == '' or nota == ' ':
            return 0
        if re.search(r'[a-zA-Z]', nota) or nota == '':
            return 1
        else:
            if ',' in nota:
                nota = nota.replace(',','.')
            nota = float(nota)
            notas_user[indice]['Nota1'].append(nota)
            del notas_user[indice]['Nota1'][0]
            notas_completas[self.email] = notas_user
            with open('notas.json', 'w', encoding='utf-8') as arq:
                json.dump(notas_completas, arq, indent=4, ensure_ascii=False)
            return 2
        
    def editar_nota2(self, nota, indice,):
        notas_completas = carregar_notas(self.email)
        notas_user = notas_completas[self.email]
        chaves_disciplinas = ['PORTUGUES', 'MATEMATICA', 'HISTORIA', 'GEOGRAFIA', 'CIENCIAS',
                                'EDUCACAOFISICA', 'ARTE', 'INGLES', 'ESPANHOL', 'FILOSOFIA']
        indice = int(indice)
        indice = chaves_disciplinas[indice - 1]
        if nota == '' or nota == ' ':
            return 0
        if re.search(r'[a-zA-Z]', nota) or nota == '':
            return 1
        else:
            if ',' in nota:
                nota = nota.replace(',','.')
            nota = float(nota)
            notas_user[indice]['Nota2'].append(nota)
            del notas_user[indice]['Nota2'][0]
            notas_completas[self.email] = notas_user
            with open('notas.json', 'w', encoding='utf-8') as arq:
                json.dump(notas_completas, arq, indent=4, ensure_ascii=False)
            return 2