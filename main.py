from cadastro import Usuario
from time import sleep
from tarefas import Tarefas
from verificacoes import Verificacao
from lembretes import carregar_lembretes, Lembrete
from cronograma import Cronograma
from notas import Notas, carregar_notas
import customtkinter as ctk
from tkinter import ttk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Ninho Desk')
        self.geometry('1280x720')
        self.frame_atual = None
        self.tela_inicial()

    def trocar_tela(self, nova_tela):
        if self.frame_atual:
            self.frame_atual.destroy()
        self.frame_atual = nova_tela
        self.frame_atual.pack(expand=True, fill='both')

    def tabela_tarefas(self, frame, email, status, prioridade):
        tarefas = Tarefas(email)
        label_titulo_crono = ctk.CTkLabel(frame, text=f'TAREFAS {status.upper()} - PRIORIDADE {prioridade.upper()}', font=('Ubuntu', 20),
                                          width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_titulo_crono.pack(pady=30)
        frame_pendente_alta = ctk.CTkFrame(frame, width=700, height=480)
        frame_pendente_alta.pack()
        resultado = tarefas.conferir_tarefas()
        resultado = resultado[status][prioridade]
        colunas = ('Título', 'Descrição', 'Data', 'Prioridade')
        tabela_pendente_alta = ttk.Treeview(
            frame_pendente_alta, columns=colunas, show='headings')
        tabela_pendente_alta.pack(fill='both')
        for col in colunas:
            tabela_pendente_alta.heading(col, text=col)
            tabela_pendente_alta.column(
                col, width=300, anchor='center', stretch=False)

        for indice in range(len(resultado)):
            tabela_pendente_alta.insert("", 'end', values=(resultado[indice]['Título'], resultado[indice]['Descrição'],
                                                           resultado[indice]['Data'], resultado[indice]['Prioridade']))
        scrollbar_horizontal = ttk.Scrollbar(
            frame_pendente_alta, orient='horizontal', command=tabela_pendente_alta.xview)
        scrollbar_horizontal.pack(side='bottom', fill='x')

    def tabela_notas(self, email, frame):
        notas = carregar_notas(email)
        notas_email = notas[email]
        frame_tabela = ctk.CTkFrame(
            frame, height=650, width=150, fg_color="transparent")
        frame_tabela.pack(padx=10, pady=10)
        colunas = ('Índice', 'Disciplina', 'Nota 1', 'Nota 2', 'Média')
        tabela_notas = ttk.Treeview(
            frame_tabela, columns=colunas, show='headings')
        for col in colunas:
            tabela_notas.heading(col, text=col)
            tabela_notas.column(col, width=150, anchor='center', stretch=False)

        tabela_notas.pack(pady=20)
        chaves = list(notas_email)
        for indice in range(len(chaves)):
            tabela_notas.insert("", "end", values=(
                f'{indice+1}', f'{chaves[indice]}', *
                notas_email[chaves[indice]]['Nota1'],
                *notas_email[chaves[indice]]['Nota2'],
                round((float(notas_email[chaves[indice]]['Nota1'][0]) + float(notas_email[chaves[indice]]['Nota2'][0]))/2, 1)))

    def tela_inicial(self):
        frame = ctk.CTkFrame(self)
        label_textoinicial = ctk.CTkLabel(frame, text='Bem-vindo ao Ninho Desk!\n'
                                          'Seu app de gerenciamento de tarefas com foco para\n as '
                                          'crianças do Ensino Fundamental com suporte e\n'
                                          'controle dos pais nas atividades e rotina dos filhos.', font=('Ubuntu', 20),
                                          width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_textoinicial.pack(pady=30)

        botao_login = ctk.CTkButton(frame, width=200, height=50, text='LOGIN', font=(
            'Roboto', 15), command=self.login)
        botao_login.pack(pady=30)

        botao_cadastro_usuario = ctk.CTkButton(frame, width=200, height=50, text='CADASTRAR\n NOVO USUÁRIO', font=(
            'Roboto', 15), command=self.cadastrar_usuario)
        botao_cadastro_usuario.pack()

        botao_cadastro_usuario = ctk.CTkButton(frame, width=200, height=50, text='SAIR', font=(
            'Roboto', 15), command=self.fechar_app)
        botao_cadastro_usuario.pack(pady=30)
        self.trocar_tela(frame)

    def fechar_app(self):
        self.destroy()

    def login(self):
        frame = ctk.CTkFrame(self)
        self.var_senha = ctk.BooleanVar(value=False)
        label_texto = ctk.CTkLabel(frame, text='Seja bem-vindo ao Ninho Desk🦉\n '
                                   'Seu APP de gerenciamento acadêmico!\n'
                                   'Vamos iniciar?', font=('Ubuntu', 20), width=640, height=80, bg_color='#3a3b3c')
        label_texto.pack(pady=30)
        label_email = ctk.CTkLabel(frame, text='EMAIL', font=(
            'Roboto', 15), width=500, height=80)
        label_email.pack()
        self.campo_email = ctk.CTkEntry(frame, placeholder_text='Digite seu email', font=(
            'Meera', 25), width=300, height=50)
        self.campo_email.pack(pady=10)

        label_senha = ctk.CTkLabel(frame, text='SENHA', font=(
            'Roboto', 15), width=500, height=80)
        label_senha.pack()

        self.campo_senha = ctk.CTkEntry(frame, placeholder_text='Digite sua senha', font=(
            'Meera', 25), width=300, height=50, show='*')
        self.campo_senha.pack(pady=10)

        check_senha = ctk.CTkCheckBox(
            frame, text='Exibir senha', variable=self.var_senha, command=self.mostrar_senha)
        check_senha.pack(pady=10)

        # Botão de login
        botao_login = ctk.CTkButton(frame, width=200, height=50, text='LOGIN', font=(
            'Roboto', 15), command=self.verificacoes)
        botao_login.pack(pady=30)

        frame_botao = ctk.CTkFrame(frame, fg_color="transparent")
        frame_botao.pack(pady=10)
        botao_esqueceu_senha = ctk.CTkButton(frame_botao, width=200, height=50, text='ESQUECEU A SENHA', font=(
            'Roboto', 15), command=self.esqueceu_senha)
        botao_esqueceu_senha.pack(side='left', padx=50)

        # Botão para voltar para a tela inicial
        botao_voltar = ctk.CTkButton(frame_botao, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=self.tela_inicial)
        botao_voltar.pack(side='right', padx=50)

        # Label de erro
        self.label_erro = ctk.CTkLabel(frame, text='')
        self.label_erro.pack(pady=10)
        self.trocar_tela(frame)

    def verificacoes(self):
        email = self.campo_email.get()
        senha = self.campo_senha.get()
        validacao = Verificacao(email, senha)
        erros = []
        resultado_email = validacao.verifica_email_login()
        if not resultado_email:
            erros.append('Email não informado')
        else:
            resultado_senha = validacao.verificar_senha()
            if not resultado_senha:
                erros.append('Senha incorreta')

        if erros:
            self.label_erro.configure(text='\n'.join(
                erros), text_color='red', font=('Meera', 20))
        else:
            self.label_erro.configure(
                text='Dados corretos!', text_color='green', font=('Meera', 20))
            sleep(1)
            self.menu_principal(email)

    def esqueceu_senha(self):
        frame = ctk.CTkFrame(self)
        self.var_senha = ctk.BooleanVar(value=False)
        self.var_confirma_senha = ctk.BooleanVar(value=False)
        label_email = ctk.CTkLabel(frame, text='EMAIL', font=(
            'Roboto', 15), width=500, height=80)
        label_email.pack()
        self.campo_email = ctk.CTkEntry(frame, placeholder_text='Digite seu email', font=(
            'Meera', 25), width=300, height=50)
        self.campo_email.pack(pady=10)
        label_senha = ctk.CTkLabel(frame, text='SENHA', font=(
            'Roboto', 15), width=400, height=60)
        label_senha.pack()
        self.campo_senha = ctk.CTkEntry(
            frame, show="*", placeholder_text='Digite sua senha min.: 8 caracteres', font=('Meera', 18), width=300, height=50)
        self.campo_senha.pack(pady=10)
        check_senha = ctk.CTkCheckBox(
            frame, text='Exibir senha', variable=self.var_senha, command=self.mostrar_senha)
        check_senha.pack(pady=10)
        label_confirma_senha = ctk.CTkLabel(
            frame, text='CONFIRME SUA SENHA', font=('Roboto', 15), width=400, height=60)
        label_confirma_senha.pack()
        self.campo_confirma_senha = ctk.CTkEntry(
            frame, show='*', placeholder_text='Confirme sua senha', font=('Meera', 20), width=300, height=50)
        self.campo_confirma_senha.pack(pady=15)
        check_senha = ctk.CTkCheckBox(
            frame, text='Exibir senha', variable=self.var_confirma_senha, command=self.mostrar_senha_confirmada)
        check_senha.pack(pady=10)

        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=self.redefinindo)
        botao_confirmar.pack(pady=20)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=self.login)
        botao_voltar.pack()

        self.label_senha_redefinida = ctk.CTkLabel(
            frame, text='', text_color='green', font=('Meera', 20))
        self.label_senha_redefinida.pack()
        self.trocar_tela(frame)

    def redefinindo(self):
        email = self.campo_email.get()
        senha = self.campo_senha.get()
        erros = []
        confirmacao = self.campo_confirma_senha.get()
        verifica_email = Verificacao(email)
        validacao = Usuario(email=email, senha=senha,
                            confirma_senha=confirmacao)
        resultado_email = verifica_email.verifica_email_login()

        if not resultado_email:
            erros.append('Email não cadastrado')
        else:
            resultado = validacao.redefinir_senha()
            if resultado == 0:
                erros.append('Senha vazia, tente novamente')
                self.campo_senha.delete(0, 'end')
                self.campo_confirma_senha.delete(0, 'end')
            elif resultado == 1:
                erros.append('Senha muito curta, tente novamente')
                self.campo_senha.delete(0, 'end')
                self.campo_confirma_senha.delete(0, 'end')
            elif resultado == 2:
                erros.append('Senhas diferentes, tente novaemnte')
                self.campo_senha.delete(0, 'end')
                self.campo_confirma_senha.delete(0, 'end')

        if erros:
            self.label_senha_redefinida.configure(text='\n'.join(
                erros), text_color='red', font=('Meera', 20))  # Exibe as mensagens de erro
        else:
            self.label_senha_redefinida.configure(
                text='Dados corretos, siga para a próxima etapa', text_color='green', font=('Meera', 20))
            sleep(1)
            self.login()

    def cadastrar_usuario(self):
        frame = ctk.CTkFrame(self)
        label_texto = ctk.CTkLabel(frame, text='CADASTRO DE USUÁRIO', font=(
            'Ubuntu', 20), width=650, height=50)
        label_texto.pack(pady=18)
        frame_insercao = ctk.CTkFrame(frame, width=650, height=100)
        frame_insercao.pack()

        label_nome = ctk.CTkLabel(frame_insercao, text='NOME', font=(
            'Roboto', 15), width=400, height=60)
        label_nome.pack()

        self.campo_nome = ctk.CTkEntry(frame_insercao, placeholder_text='Digite seu nome (limite de 20 caracteres)', font=(
            'Meera', 18), width=300, height=50)
        self.campo_nome.pack(pady=10)

        label_email = ctk.CTkLabel(frame_insercao, text='EMAIL', font=(
            'Roboto', 15), width=400, height=60)
        label_email.pack()

        self.campo_email = ctk.CTkEntry(frame_insercao, placeholder_text='Digite seu email', font=(
            'Meera', 20), width=300, height=50)
        self.campo_email.pack(pady=15)
        label_serie = ctk.CTkLabel(frame_insercao, text='SÉRIE DA CRIANÇA', font=(
            'Roboto', 15), width=400, height=60)
        label_serie.pack()
        self.campo_serie = ctk.CTkEntry(frame_insercao, placeholder_text='Digite a série da criança', font=(
            'Meera', 20), width=300, height=50)
        self.campo_serie.pack(pady=15)

        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=self.validar_pt1_cadastro)
        botao_confirmar.pack(pady=20)


        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=self.tela_inicial)
        botao_voltar.pack()

        self.label_confirma = ctk.CTkLabel(frame, text='')
        self.label_confirma.pack()
        self.trocar_tela(frame)

    def validar_pt1_cadastro(self):
        nome = self.campo_nome.get()
        email = self.campo_email.get()
        serie = self.campo_serie.get()
        usuario = Usuario(nome, email, serie)
        resultado_nome = usuario.validar_nome()
        resultado_email = usuario.validar_email()
        resultado_serie = usuario.validar_serie()
        erros = []
        if not resultado_nome:
            erros.append('Nome de usuário incorreto')
            self.campo_nome.delete(0, 'end')

        if resultado_email == 1:
            erros.append('Email já cadastrado, insira um email novo')
            self.campo_email.delete(0, 'end')
        elif resultado_email == 2:
            erros.append('Email inválido, insira um email válido')
            self.campo_email.delete(0, 'end')

        if not resultado_serie:
            erros.append('Série inválida! Informe uma série válida')
            self.campo_serie.delete(0, 'end')

        if erros:
            self.label_confirma.configure(text='\n'.join(
                erros), text_color='red', font=('Meera', 20))
        else:
            self.label_confirma.configure(
                text='Dados corretos, siga para a próxima etapa', text_color='green', font=('Meera', 20))
            self.cadastrar_usuario_pt2(nome, email, serie)

    def mostrar_senha(self):
        if self.var_senha.get():
            try:
                self.campo_senha.configure(show='')
            except:
                self.campo_senha_mestre.configure(show='')
        else:
            try:
                self.campo_senha.configure(show='*')
            except:
                self.campo_senha_mestre.configure(show='*')

    def mostrar_senha_confirmada(self):
        if self.var_confirma_senha.get():
            try:
                self.campo_confirma_senha.configure(show='')
            except:
                self.campo_confirma_senha_mestre.configure(show='')
        else:
            try:
                self.campo_confirma_senha.configure(show='*')
            except:
                self.campo_confirma_senha_mestre.configure(show='*')

    def cadastrar_usuario_pt2(self, nome, email, serie):
        frame = ctk.CTkFrame(self)
        self.var_senha = ctk.BooleanVar(value=False)
        self.var_confirma_senha = ctk.BooleanVar(value=False)
        label_texto = ctk.CTkLabel(frame, text='CADASTRO DE USUÁRIO', font=(
            'Ubuntu', 20), width=650, height=50)
        label_texto.pack(pady=18)
        frame_insercao = ctk.CTkFrame(frame, width=650, height=100)
        frame_insercao.pack()
        label_senha = ctk.CTkLabel(frame_insercao, text='SENHA', font=(
            'Roboto', 15), width=400, height=60)
        label_senha.pack()
        self.campo_senha = ctk.CTkEntry(
            frame_insercao, show="*", placeholder_text='Digite sua senha min.: 8 caracteres', font=('Meera', 18), width=300, height=50)
        self.campo_senha.pack(pady=10)
        check_senha = ctk.CTkCheckBox(
            frame_insercao, text='Exibir senha', variable=self.var_senha, command=self.mostrar_senha)
        check_senha.pack(pady=10)
        label_confirma_senha = ctk.CTkLabel(
            frame_insercao, text='CONFIRME SUA SENHA', font=('Roboto', 15), width=400, height=60)
        label_confirma_senha.pack()
        self.campo_confirma_senha = ctk.CTkEntry(
            frame_insercao, show='*', placeholder_text='Confirme sua senha', font=('Meera', 20), width=300, height=50)
        self.campo_confirma_senha.pack(pady=15)
        check_senha = ctk.CTkCheckBox(frame_insercao, text='Exibir senha',
                                      variable=self.var_confirma_senha, command=self.mostrar_senha_confirmada)
        check_senha.pack(pady=10)

        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=lambda: self.validar_pt2_cadastro(nome, email, serie))
        botao_confirmar.pack(pady=20)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=self.cadastrar_usuario)
        botao_voltar.pack()

        self.label_confirma = ctk.CTkLabel(
            frame, text='', text_color='green', font=('Meera', 20))
        self.label_confirma.pack()
        self.trocar_tela(frame)

    def validar_pt2_cadastro(self, nome, email, serie):
        senha = self.campo_senha.get()
        confirma_senha = self.campo_confirma_senha.get()
        erros = []  # Lista que guarda as mensagens de erro
        usuario = Usuario(senha=senha, confirma_senha=confirma_senha)
        resultado = usuario.cadastrar_senha()

        if resultado == 0:
            erros.append('Senha vazia, tente novamente')
            self.campo_senha.delete(0, 'end')
            self.campo_confirma_senha.delete(0, 'end')
        elif resultado == 1:
            erros.append('Senha muito curta, tente novamente')
            self.campo_senha.delete(0, 'end')
            self.campo_confirma_senha.delete(0, 'end')
        elif resultado == 2:
            erros.append('Senhas diferentes, tente novaemnte')
            self.campo_senha.delete(0, 'end')
            self.campo_confirma_senha.delete(0, 'end')

        if erros:
            self.label_confirma.configure(text='\n'.join(erros), text_color='red', font=(
                'Meera', 20))  # Exibe as mensagens de erro
        else:
            self.label_confirma.configure(
                text='Dados corretos, siga para a próxima etapa', text_color='green', font=('Meera', 20))
            self.cadastrar_usuario_pt3(nome, email, serie, senha)

    def cadastrar_usuario_pt3(self, nome, email, serie, senha):
        frame = ctk.CTkFrame(self)
        self.var_senha = ctk.BooleanVar(value=False)
        self.var_confirma_senha = ctk.BooleanVar(value=False)
        label_texto = ctk.CTkLabel(frame, text='CADASTRO DE USUÁRIO', font=(
            'Ubuntu', 20), width=650, height=50)
        label_texto.pack(pady=18)
        frame_insercao = ctk.CTkFrame(frame, width=650, height=100)
        frame_insercao.pack()
        
        label_senha_mestre = ctk.CTkLabel(
            frame_insercao, text='SENHA MESTRE', font=('Roboto', 15), width=400, height=60)
        label_senha_mestre.pack()
        label_explica_senha_mestre = ctk.CTkLabel(
            frame_insercao, text='(Senha utilizada para acessar o Controle dos Pais)')
        label_explica_senha_mestre.pack()
        self.campo_senha_mestre = ctk.CTkEntry(
            frame_insercao, show="*", placeholder_text='Digite sua senha. min.: 9 caracteres e letra', font=('Meera', 18), width=300, height=50)
        self.campo_senha_mestre.pack(pady=10)
        check_senha_mestre = ctk.CTkCheckBox(
            frame_insercao, text='Exibir senha', variable=self.var_senha, command=self.mostrar_senha)
        check_senha_mestre.pack(pady=10)
        label_confirma_senha_mestre = ctk.CTkLabel(
            frame_insercao, text='CONFIRME SUA SENHA', font=('Roboto', 15), width=400, height=60)
        label_confirma_senha_mestre.pack()
        self.campo_confirma_senha_mestre = ctk.CTkEntry(
            frame_insercao, show='*', placeholder_text='Confirme sua senha', font=('Meera', 20), width=300, height=50)
        self.campo_confirma_senha_mestre.pack(pady=15)
        check_senha_mestre = ctk.CTkCheckBox(
            frame_insercao, text='Exibir senha', variable=self.var_confirma_senha, command=self.mostrar_senha_confirmada)
        check_senha_mestre.pack(pady=10)

        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=lambda: self.validar_pt3_cadastro(nome, email, serie, senha))
        botao_confirmar.pack(pady=20)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.cadastrar_usuario_pt2(nome, email, serie))
        botao_voltar.pack()

        self.label_confirma = ctk.CTkLabel(
            frame, text='', text_color='green', font=('Meera', 20))
        self.label_confirma.pack()
        self.trocar_tela(frame)

    def validar_pt3_cadastro(self, nome, email, serie, senha):
        nome_usuario = nome
        email_usuario = email
        serie_usuario = serie
        senha_usuario = senha
        senha_mestre = self.campo_senha_mestre.get()
        confirma_senha_mestre = self.campo_confirma_senha_mestre.get()
        erros = []  # Lista que guarda as mensagens de erro
        usuario = Usuario(nome=nome_usuario, email=email_usuario, senha=senha_usuario,
                          serie=serie_usuario, senha_mestre=senha_mestre, confirma_senha_mestre=confirma_senha_mestre)
        resultado = usuario.cadastrar_senha_mestre()

        if resultado == 0:
            erros.append('Senha vazia, tente novamente')
            self.campo_senha_mestre.delete(0, 'end')
            self.campo_confirma_senha_mestre.delete(0, 'end')
        elif resultado == 1:
            erros.append('Senha muito curta, tente novamente')
            self.campo_senha_mestre.delete(0, 'end')
            self.campo_confirma_senha_mestre.delete(0, 'end')
        elif resultado == 2:
            erros.append('Senha não possui letra, tente novaemnte')
            self.campo_senha_mestre.delete(0, 'end')
            self.campo_confirma_senha_mestre.delete(0, 'end')
        elif resultado == 3:
            erros.append('Senha não possui número, tente novaemnte')
            self.campo_senha_mestre.delete(0, 'end')
            self.campo_confirma_senha_mestre.delete(0, 'end')
        elif resultado == 4:
            erros.append('Senhas diferentes, tente novaemnte')
            self.campo_senha_mestre.delete(0, 'end')
            self.campo_confirma_senha_mestre.delete(0, 'end')

        if erros:
            self.label_confirma.configure(text='\n'.join(erros), text_color='red', font=(
                'Meera', 20))  # Exibe as mensagens de erro
        else:
            self.label_confirma.configure(
                text='Dados corretos, siga para a próxima etapa', text_color='green', font=('Meera', 20))
            usuario.salvar_dados()
            self.menu_principal(email)

    def menu_principal(self, email):
        frame = ctk.CTkFrame(self)
        label_titulo_menu = ctk.CTkLabel(frame, text='MENU DO ESTUDANTE', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_titulo_menu.pack(pady=30)

        botao_conferir_tarefas = ctk.CTkButton(
            frame, width=200, height=50, text='CONFERIR TAREFAS', font=('Roboto', 15), command=lambda: self.conferir_tarefas(email))
        botao_conferir_tarefas.pack(pady=10)

        botao_ver_cronograma = ctk.CTkButton(frame, width=200, height=50, text='VER CRONOGRAMA', font=(
            'Roboto', 15), command=lambda: self.ver_cronograma(email))
        botao_ver_cronograma.pack(pady=10)

        botao_ver_lembrete = ctk.CTkButton(frame, width=200, height=50, text='VER LEMBRETES', font=(
            'Roboto', 15), command=lambda: self.ver_lembretes(email))
        botao_ver_lembrete.pack(pady=10)

        botao_controle_pais = ctk.CTkButton(frame, width=200, height=50, text='CONTROLE DOS PAIS', font=(
            'Roboto', 15), command=lambda: self.controle_pais(email))
        botao_controle_pais.pack(pady=10)

        botao_ver_notas = ctk.CTkButton(frame, width=200, height=50, text='VER NOTAS', font=(
            'Roboto', 15), command=lambda: self.notas(email))
        botao_ver_notas.pack(pady=10)

        botao_editar_perfil = ctk.CTkButton(frame, width=200, height=50, text='EDITAR PERFIL', font=(
            'Roboto', 15), command=lambda: self.editar_perfil(email))
        botao_editar_perfil.pack(pady=10)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=self.login)
        botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def conferir_tarefas(self, email):
        frame = ctk.CTkFrame(self)
        label_titulo_crono = ctk.CTkLabel(frame, text='TAREFAS', font=('Ubuntu', 20),
                                          width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_titulo_crono.pack()
        botao_pendente = ctk.CTkButton(frame, width=200, height=50, text='TAREFAS PENDENTES', font=(
            'Roboto', 15), command=lambda: self.tarefas_pendentes(email, 0))
        botao_pendente.pack(pady=10)

        botao_concluido = ctk.CTkButton(frame, width=200, height=50, text='TAREFAS CONCLUIDAS', font=(
            'Roboto', 15), command=lambda: self.tarefas_concluidas(email))
        botao_concluido.pack(pady=10)

        botao_concluido = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.menu_principal(email))
        botao_concluido.pack(pady=10)
        self.trocar_tela(frame)

    def tarefas_pendentes(self, email, contador):
        frame = ctk.CTkFrame(self)
        status = 'Pendente'
        prioridade = 'ALTA'
        self.tabela_tarefas(frame, email, status, prioridade)
        if contador == 0:
            botao_pendente_media = ctk.CTkButton(frame, width=200, height=50, text='PRIORIDADE MÉDIA', font=(
            'Roboto', 15), command=lambda: self.tarefas_pendentes2(email, 0))
            botao_pendente_media.pack(pady=10)
            botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
                'Roboto', 15), command=lambda: self.conferir_tarefas(email))
            botao_voltar.pack(pady=10)
        elif contador == 1:
            botao_pendente_media = ctk.CTkButton(frame, width=200, height=50, text='PRIORIDADE MÉDIA', font=(
            'Roboto', 15), command=lambda: self.tarefas_pendentes2(email, 1))
            botao_pendente_media.pack(pady=10)
            botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
                'Roboto', 15), command=lambda: self.tela_editar_tarefa(email))
            botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def tarefas_pendentes2(self, email, contador):
        frame = ctk.CTkFrame(self)
        status = 'Pendente'
        prioridade = 'MEDIA'
        self.tabela_tarefas(frame, email, status, prioridade)
        
        if contador == 0:
            botao_pendente_baixa = ctk.CTkButton(frame, width=200, height=50, text='PRIORIDADE BAIXA', font=(
            'Roboto', 15), command=lambda: self.tarefas_pendentes3(email, 0))
            botao_pendente_baixa.pack(pady=10)
            botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
                'Roboto', 15), command=lambda: self.tarefas_pendentes(email, 0))
            botao_voltar.pack(pady=10)
        elif contador == 1:
            botao_pendente_baixa = ctk.CTkButton(frame, width=200, height=50, text='PRIORIDADE BAIXA', font=(
            'Roboto', 15), command=lambda: self.tarefas_pendentes3(email, 1))
            botao_pendente_baixa.pack(pady=10)
            botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
                'Roboto', 15), command=lambda: self.tarefas_pendentes(email, 1))
            botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def tarefas_pendentes3(self, email, contador):
        frame = ctk.CTkFrame(self)
        status = 'Pendente'
        prioridade = 'BAIXA'
        self.tabela_tarefas(frame, email, status, prioridade)
        if contador == 0:
            botao_pendente_spriori = ctk.CTkButton(frame, width=200, height=50, text='SEM PRIORIDADE', font=(
                'Roboto', 15), command=lambda: self.tarefas_pendentes4(email, 0))
            botao_pendente_spriori.pack(pady=10)
            botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
                'Roboto', 15), command=lambda: self.tarefas_pendentes2(email, 0))
            botao_voltar.pack(pady=10)
        elif contador == 1:
            botao_pendente_spriori = ctk.CTkButton(frame, width=200, height=50, text='SEM PRIORIDADE', font=(
                'Roboto', 15), command=lambda: self.tarefas_pendentes4(email, 1))
            botao_pendente_spriori.pack(pady=10)
            botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
                'Roboto', 15), command=lambda: self.tarefas_pendentes2(email, 1))
            botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def tarefas_pendentes4(self, email, contador):
        frame = ctk.CTkFrame(self)
        status = 'Pendente'
        prioridade = 'SEM PRIORIDADE'
        self.tabela_tarefas(frame, email, status, prioridade)
        if contador == 0:
            botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
                'Roboto', 15), command=lambda: self.tarefas_pendentes3(email,0))
            botao_voltar.pack(pady=10)
        elif contador == 1:
            botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
                'Roboto', 15), command=lambda: self.tarefas_pendentes3(email,1))
            botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def tarefas_concluidas(self, email):
        frame = ctk.CTkFrame(self)
        status = 'Concluída'
        prioridade = 'ALTA'
        self.tabela_tarefas(frame, email, status, prioridade)
        botao_pendente_media = ctk.CTkButton(frame, width=200, height=50, text='PRIORIDADE MÉDIA', font=(
            'Roboto', 15), command=lambda: self.tarefas_concluidas2(email))
        botao_pendente_media.pack(pady=10)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.conferir_tarefas(email))
        botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def tarefas_concluidas2(self, email):
        frame = ctk.CTkFrame(self)
        status = 'Concluída'
        prioridade = 'MEDIA'
        self.tabela_tarefas(frame, email, status, prioridade)
        botao_pendente_baixa = ctk.CTkButton(frame, width=200, height=50, text='PRIORIDADE BAIXA', font=(
            'Roboto', 15), command=lambda: self.tarefas_concluidas3(email))
        botao_pendente_baixa.pack(pady=10)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.tarefas_concluidas(email))
        botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def tarefas_concluidas3(self, email):
        frame = ctk.CTkFrame(self)
        status = 'Concluída'
        prioridade = 'BAIXA'
        self.tabela_tarefas(frame, email, status, prioridade)
        botao_pendente_spriori = ctk.CTkButton(frame, width=200, height=50, text='SEM PRIORIDADE', font=(
            'Roboto', 15), command=lambda: self.tarefas_concluidas4(email))
        botao_pendente_spriori.pack(pady=10)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.tarefas_concluidas2(email))
        botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def tarefas_concluidas4(self, email):
        frame = ctk.CTkFrame(self)
        status = 'Concluída'
        prioridade = 'SEM PRIORIDADE'
        self.tabela_tarefas(frame, email, status, prioridade)
        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.tarefas_concluidas3(email))
        botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def ver_cronograma(self, email):
        frame = ctk.CTkFrame(self)
        label_titulo_crono = ctk.CTkLabel(frame, text='CRONOGRAMA', font=('Ubuntu', 20),
                                          width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_titulo_crono.pack(pady=30)
        botao_crono_tarefas = ctk.CTkButton(frame, width=200, height=50, text='CRONOGRAMA DE\nTAREFAS', font=(
            'Roboto', 15), command=lambda: self.crono_tarefas(email))
        botao_crono_tarefas.pack(pady=10)

        botao_crono_estudo = ctk.CTkButton(frame, width=200, height=50, text='CRONOGRAMA DE\nESTUDO', font=(
            'Roboto', 15), command=lambda: self.crono_de_estudo(email, 0))
        botao_crono_estudo.pack(pady=10)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.menu_principal(email))
        botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def crono_tarefas(self, email):
        frame = ctk.CTkFrame(self)
        crono_tarefas_lista = Cronograma(email)
        resultado_tarefas = crono_tarefas_lista.ver_cronograma_tarefas()
        label_titulo = ctk.CTkLabel(frame, text='CRONOGRAMA DE TAREFAS', font=('Ubuntu', 20),
                                    width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_titulo.pack(pady=30)

        if resultado_tarefas == 0:
            label_tarefas0 = ctk.CTkLabel(frame, text='Cronograma não criado', font=('Ubuntu', 20),
                                          width=1280, height=98, text_color='#f5f7fa')
            label_tarefas0.pack(pady=30)
        elif resultado_tarefas == 1:
            label_tarefas1 = ctk.CTkLabel(frame, text='Nenhuma tarefa pendente', font=('Ubuntu', 20),
                                          width=1280, height=98, text_color='#f5f7fa')
            label_tarefas1.pack(pady=30)
        else:
            crono_tarefas = resultado_tarefas
            frame_cronograma = ctk.CTkFrame(frame, height=300, width=100)
            frame_cronograma.pack(padx=10, pady=10, fill='both')
            colunas = list(crono_tarefas[0].keys())
            tabela_cronograma = ttk.Treeview(
                frame_cronograma, columns=colunas, show='headings')
            for col in colunas:
                tabela_cronograma.heading(col, text=col)
                tabela_cronograma.column(
                    col, width=300, anchor='center', stretch=False)

            scrollbar_vertical = ttk.Scrollbar(
                frame_cronograma, orient='vertical', command=tabela_cronograma.yview)
            scrollbar_horizontal = ttk.Scrollbar(
                frame_cronograma, orient='horizontal', command=tabela_cronograma.xview)
            scrollbar_horizontal.pack(side='bottom', fill='x')
            scrollbar_vertical.pack(side='right', fill='y', )
            tabela_cronograma.pack(fill='both', expand=True)
            linha_anterior = None
            for indice, valor in enumerate(crono_tarefas):
                for chave, valor in enumerate(crono_tarefas[indice]):
                    if linha_anterior != crono_tarefas[indice]['Título']:
                        tabela_cronograma.insert("", "end", values=(crono_tarefas[indice]['Título'], crono_tarefas[indice]['Descrição'],
                                                                    crono_tarefas[indice]['Data'], crono_tarefas[indice]['Prioridade']))
                        linha_anterior = crono_tarefas[indice]['Título']

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.ver_cronograma(email))
        botao_voltar.pack(pady=10)

        self.trocar_tela(frame)

    def crono_de_estudo(self, email, contador):
        frame = ctk.CTkFrame(self)
        crono_estudo_lista = Cronograma(email)
        resultado_estudo = crono_estudo_lista.ver_cronograma_estudos()
        label_titulo = ctk.CTkLabel(frame, text='CRONOGRAMA DE ESTUDO', font=('Ubuntu', 20),
                                    width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_titulo.pack(pady=30)

        if resultado_estudo == 0:
            label_tarefas0 = ctk.CTkLabel(frame, text='Cronograma não criado', font=('Ubuntu', 20),
                                          width=1280, height=98, text_color='#f5f7fa')
            label_tarefas0.pack(pady=30)
        else:
            crono_estudo = resultado_estudo
            frame_cronograma = ctk.CTkFrame(frame, height=150, width=30)
            frame_cronograma.pack()
            colunas = ('Dia da semana', 'Disciplina')
            tabela_cronograma = ttk.Treeview(
                frame_cronograma, columns=colunas, show='headings')
            for col in colunas:
                tabela_cronograma.heading(col, text=col)
                tabela_cronograma.column(
                    col, width=300, anchor='center', stretch=False)

            scrollbar_vertical = ttk.Scrollbar(
                frame_cronograma, orient='vertical', command=tabela_cronograma.yview)
            scrollbar_horizontal = ttk.Scrollbar(
                frame_cronograma, orient='horizontal', command=tabela_cronograma.xview)
            scrollbar_horizontal.pack(side='bottom', fill='x')
            scrollbar_vertical.pack(side='right', fill='y', )
            tabela_cronograma.pack(fill='both', expand=True)
            chaves_lista = list(crono_estudo.keys())
            for indice, chave in enumerate(crono_estudo):
                tabela_cronograma.insert("", "end", values=(
                    chaves_lista[indice], crono_estudo[chave]))
        if contador == 0:
            botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
                'Roboto', 15), command=lambda: self.ver_cronograma(email))
            botao_voltar.pack(pady=10)
        elif contador == 1:
                botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
                'Roboto', 15), command=lambda: self.organizar_cronograma(email))
                botao_voltar.pack(pady=10)

        self.trocar_tela(frame)

    def notas(self, email):
        frame = ctk.CTkFrame(self)
        label_titulo = ctk.CTkLabel(frame, text='QUADRO DE NOTAS', font=('Ubuntu', 20),
                                    width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_titulo.pack(pady=30)
        self.tabela_notas(email, frame)
        botao_editar_perfil = ctk.CTkButton(frame, width=200, height=50, text='MENU', font=(
            'Roboto', 15), command=lambda: self.menu_principal(email))
        botao_editar_perfil.pack(pady=10)

        self.trocar_tela(frame)

    def ver_lembretes(self, email):
        frame = ctk.CTkFrame(self)
        label_titulo_menu = ctk.CTkLabel(frame, text='LEMBRETES', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_titulo_menu.pack(pady=30)

        botao_lista_lembretes = ctk.CTkButton(
            frame, width=200, height=50, text='LISTA DE LEMBRETES', font=('Roboto', 15), command=lambda: self.lista_lembretes(email))
        botao_lista_lembretes.pack(pady=10)

        botao_adicionar = ctk.CTkButton(frame, width=200, height=50, text='ADICIONAR LEMBRETES', font=(
            'Roboto', 15), command=lambda: self.controle_pais(email))
        botao_adicionar.pack(pady=10)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.menu_principal(email))
        botao_voltar.pack(pady=10)

        self.trocar_tela(frame)

    def lista_lembretes(self, email):
        frame = ctk.CTkFrame(self)
        lembretes_lista = Lembrete(email)
        resultado_lembrete = lembretes_lista.lista_lembretes()
        label_titulo = ctk.CTkLabel(frame, text='QUADRO DE LEMBRETES', font=('Ubuntu', 20),
                                    width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_titulo.pack(pady=30)

        if resultado_lembrete == 0:
            label_lembrete = ctk.CTkLabel(frame, text='Nenhum lembrete encontrado', font=('Ubuntu', 20),
                                          width=1280, height=98, text_color='#f5f7fa')
            label_lembrete.pack(pady=30)
        elif resultado_lembrete == 1:
            lembretes = carregar_lembretes()
            lembretes = lembretes[email]
            frame_lembrete = ctk.CTkFrame(
                frame, height=800, width=150, fg_color="transparent")
            frame_lembrete.pack(padx=10, pady=10)
            colunas = ('Título', 'Descrição')
            tabela_lembrete = ttk.Treeview(
                frame_lembrete, columns=colunas, show='headings')
            for col in colunas:
                tabela_lembrete.heading(col, text=col)
                tabela_lembrete.column(
                    col, width=500, anchor='center', stretch=False)

            for indice in range(len(lembretes)):
                tabela_lembrete.insert("", "end", values=(lembretes[indice]['Título'], lembretes[indice]['Descrição']))
            scrollbar_horizontal = ttk.Scrollbar(
            frame_lembrete, orient='horizontal', command=tabela_lembrete.xview)
        scrollbar_horizontal.pack(side='bottom', fill='x')
        tabela_lembrete.pack(fill='both')
        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.ver_lembretes(email))
        botao_voltar.pack(pady=10)

        self.trocar_tela(frame)

    def controle_pais(self, email):
        frame = ctk.CTkFrame(self)
        self.var_senha = ctk.BooleanVar(value=False)
        self.var_confirma_senha = ctk.BooleanVar(value=False)
        label_texto = ctk.CTkLabel(frame, text='ACESSO DOS PAIS - SENHA MESTRE', font=(
            'Ubuntu', 20), width=650, height=50)
        label_texto.pack(pady=18)
        frame_insercao = ctk.CTkFrame(frame, width=650, height=100)
        frame_insercao.pack()
        
        label_senha_mestre = ctk.CTkLabel(
            frame_insercao, text='SENHA MESTRE', font=('Roboto', 15), width=400, height=60)
        label_senha_mestre.pack()
        label_explica_senha_mestre = ctk.CTkLabel(
            frame_insercao, text='(Senha utilizada para acessar o Controle dos Pais)')
        label_explica_senha_mestre.pack()
        self.campo_senha_mestre = ctk.CTkEntry(
            frame_insercao, show="*", placeholder_text='Digite sua senha. min.: 9 caracteres e letra', font=('Meera', 18), width=300, height=50)
        self.campo_senha_mestre.pack(pady=10)
        check_senha_mestre = ctk.CTkCheckBox(
            frame_insercao, text='Exibir senha', variable=self.var_senha, command=self.mostrar_senha)
        check_senha_mestre.pack(pady=10)
        label_confirma_senha_mestre = ctk.CTkLabel(
            frame_insercao, text='CONFIRME SUA SENHA', font=('Roboto', 15), width=400, height=60)
        label_confirma_senha_mestre.pack()
        self.campo_confirma_senha_mestre = ctk.CTkEntry(
            frame_insercao, show='*', placeholder_text='Confirme sua senha', font=('Meera', 20), width=300, height=50)
        self.campo_confirma_senha_mestre.pack(pady=15)
        check_senha_mestre = ctk.CTkCheckBox(
            frame_insercao, text='Exibir senha', variable=self.var_confirma_senha, command=self.mostrar_senha_confirmada)
        check_senha_mestre.pack(pady=10)

        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=lambda: self.direciona_menu_pais(email))
        botao_confirmar.pack(pady=20)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.menu_principal(email))
        botao_voltar.pack()

        self.label_confirma = ctk.CTkLabel(
            frame, text='', text_color='green', font=('Meera', 20))
        self.label_confirma.pack()
        self.trocar_tela(frame)

    def direciona_menu_pais(self, email):
        senha_mestre = self.campo_senha_mestre.get()
        confirma_senha_mestre = self.campo_confirma_senha_mestre.get()
        verificar_senha = Verificacao(
            email, senha_mestre, confirma_senha_mestre)
        resultado = verificar_senha.verificar_senha_master()
        erros = []
        if resultado == 1:
            erros.append('Senhas diferentes')
            self.campo_senha_mestre.delete(0, 'end')
            self.campo_confirma_senha_mestre.delete(0, 'end')
        elif resultado == 2:
            erros.append('Senha incorreta')
            self.campo_senha_mestre.delete(0, 'end')
            self.campo_confirma_senha_mestre.delete(0, 'end')

        if erros:
            self.label_confirma.configure(text='\n'.join(erros), text_color='red', font=(
                'Meera', 20))  # Exibe as mensagens de erro
        else:
            self.label_confirma.configure(
                text='Senha correta', text_color='green', font=('Meera', 20))
            self.menu_pais(email)

    def menu_pais(self, email):
        frame = ctk.CTkFrame(self)
        label_menu_pais = ctk.CTkLabel(frame, text='MENU DOS PAIS', font=(
            'Ubuntu', 20), width=650, height=50)
        label_menu_pais.pack(pady=18)
        botao_admin_tarefa = ctk.CTkButton(frame, width=200, height=50, text='ADMINISTRAR TAREFAS', font=(
            'Roboto', 15), command=lambda: self.administrar_tarefas(email))
        botao_admin_tarefa.pack(pady=10)

        botao_organ_crono = ctk.CTkButton(frame, width=200, height=50, text='ORGANIZAR\nCRONOGRAMA', font=(
            'Roboto', 15), command=lambda: self.organizar_cronograma(email))
        botao_organ_crono.pack(pady=10)

        botao_editar_nota = ctk.CTkButton(frame, width=200, height=50, text='EDITAR NOTAS', font=(
            'Roboto', 15), command=lambda: self.editar_notas(email))
        botao_editar_nota.pack(pady=10)

        botao_criar_lembrete = ctk.CTkButton(frame, width=200, height=50, text='CRIAR LEMBRETES', font=(
            'Roboto', 15), command=lambda: self.tela_add_lembrete(email))
        botao_criar_lembrete.pack(pady=10)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=self.login)
        botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def administrar_tarefas(self, email):
        frame = ctk.CTkFrame(self)
        label_menu_pais = ctk.CTkLabel(frame, text='ADMINISTRAR TAREFAS', font=(
            'Ubuntu', 20), width=650, height=50)
        label_menu_pais.pack(pady=30)
        botao_editar_nota = ctk.CTkButton(frame, width=200, height=50, text='CRIAR NOVA TAREFA', font=(
            'Roboto', 15), command=lambda: self.tela_criar_tarefa(email))
        botao_editar_nota.pack(pady=10)

        botao_criar_lembrete = ctk.CTkButton(frame, width=200, height=50, text='EDITAR TAREFA', font=(
            'Roboto', 15), command=lambda: self.tela_editar_tarefa(email))
        botao_criar_lembrete.pack(pady=10)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.menu_pais(email))
        botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def tela_criar_tarefa(self, email):
        frame = ctk.CTkFrame(self)
        label_criar_tarefa = ctk.CTkLabel(frame, text='CRIAR TAREFA', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_criar_tarefa.pack(pady=30)
        label_titulo = ctk.CTkLabel(frame, text='Título da Tarefa', font=('Ubuntu', 20))
        label_titulo.pack(pady=10)
        self.entry_titulo = ctk.CTkEntry(frame, placeholder_text='Informe o título da tarefa', font=('Meera', 18), width=300, height=50)
        self.entry_titulo.pack()

        label_descricao = ctk.CTkLabel(frame, text='Descrição da Tarefa', font=('Ubuntu', 20))
        label_descricao.pack(pady=10)
        self.entry_descricao = ctk.CTkEntry(frame, placeholder_text='Informe a descrição da tarefa', font=('Meera', 18), width=300, height=50)
        self.entry_descricao.pack()

        label_data = ctk.CTkLabel(frame, text='Prazo da Tarefa', font=('Ubuntu', 20))
        label_data.pack(pady=10)
        self.entry_data = ctk.CTkEntry(frame, placeholder_text='DD/MM/AAAA', font=('Meera', 18), width=300, height=50)
        self.entry_data.pack()

        label_prioridade = ctk.CTkLabel(frame, text='Prioridade da Tarefa\n(ESCREVA COMO INDICADO NO CAMPO)', font=('Ubuntu', 17))
        label_prioridade.pack(pady=10)
        self.entry_prioridade = ctk.CTkEntry(frame, placeholder_text='(ALTA/ MEDIA/ BAIXA/ SEM PRIORIDADE)', font=('Meera', 18), width=300, height=50)
        self.entry_prioridade.pack()

        frame_botoes = ctk.CTkFrame(frame, fg_color='transparent')
        frame_botoes.pack(pady=10)
        botao_confirma = ctk.CTkButton(frame_botoes, text='CRIAR', command=lambda: self.criar_tarefa(email), width=200, height=50, font=(
            'Roboto', 15))
        botao_confirma.pack(padx=10, side='left')
        botao_voltar = ctk.CTkButton(frame_botoes, text='VOLTAR', command=lambda: self.administrar_tarefas(email), width=200, height=50, font=(
            'Roboto', 15))
        botao_voltar.pack(padx=10, side='right')
        self.label_confirma_tarefa = ctk.CTkLabel(frame, text='')
        self.label_confirma_tarefa.pack(pady=10)
        self.trocar_tela(frame)
    
    def criar_tarefa(self, email):
        tarefas_objeto = Tarefas(email)
        titulo = self.entry_titulo.get()
        descricao = self.entry_descricao.get()
        data = self.entry_data.get()
        prioridade = self.entry_prioridade.get()
        erros = []
        resultado = tarefas_objeto.criar_tarefas(titulo, descricao, data, prioridade)
        if resultado == 0:
            erros.append('Título vazio')
            self.entry_titulo.delete(0, 'end')
        elif resultado == 1:
            erros.append('Descrição vazio')
            self.entry_descricao.delete(0, 'end')
        elif resultado == 2:
            erros.append('Data com formato inválido')
            self.entry_data.delete(0, 'end')
        elif resultado == 3:
            erros.append('Data anterior a hoje')
            self.entry_prioridade.delete(0, 'end')
        elif resultado == 4:
            erros.append('Prioridade com formato inválido')
            self.entry_prioridade.delete(0, 'end')
        
        if erros:
            self.label_confirma_tarefa.configure(text='\n'.join(erros), text_color='red', font=(
                'Meera', 20))  # Exibe as mensagens de erro
        else:
            self.label_confirma_tarefa.configure(
                text='TAREFA CRIADA COM SUCESSO!', text_color='green', font=('Meera', 20))
            tarefas_objeto.salvar_tarefas(titulo, descricao, data, prioridade)

    def tela_editar_tarefa(self, email):
        frame = ctk.CTkFrame(self)
        label_editar_tarefa = ctk.CTkLabel(frame, text='EDITAR TAREFA', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_editar_tarefa.pack(pady=30)
        botao_editar_titulo = ctk.CTkButton(frame, width=200, height=50, text='EDITAR TÍTULO', font=(
            'Roboto', 15), command=lambda: self.editar_titulo(email))
        botao_editar_titulo.pack(pady=10)

        botao_editar_descricao = ctk.CTkButton(frame, width=200, height=50, text='EDITAR DESCRIÇÃO', font=(
            'Roboto', 15), command=lambda: self.editar_descricao(email))
        botao_editar_descricao.pack(pady=10)

        botao_editar_prazo = ctk.CTkButton(frame, width=200, height=50, text='EDITAR PRAZO', font=(
            'Roboto', 15), command=lambda: self.editar_prazo(email))
        botao_editar_prazo.pack(pady=10)

        botao_editar_prioridade = ctk.CTkButton(frame, width=200, height=50, text='EDITAR PRIORIDADE', font=(
            'Roboto', 15), command=lambda: self.editar_prioridade(email))
        botao_editar_prioridade.pack(pady=10)

        botao_apagar_tarefa = ctk.CTkButton(frame, width=200, height=50, text='APAGAR TAREFA', font=(
            'Roboto', 15), command=lambda:  self.apagar_tarefa(email))
        botao_apagar_tarefa.pack(pady=10)

        botao_visualizar_tarefas = ctk.CTkButton(frame, width=200, height=50, text='VER TAREFAS PENDENTES', font=(
            'Roboto', 15), command=lambda:  self.tarefas_pendentes(email, 1))
        botao_visualizar_tarefas.pack(pady=10)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.administrar_tarefas(email))
        botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def editar_titulo(self, email):
        frame = ctk.CTkFrame(self)
        label_titulo_antigo = ctk.CTkLabel(frame, text='Título da tarefa que deseja mudar', font=('Ubuntu', 17))
        label_titulo_antigo.pack(pady=50)
        self.entry_titulo_antigo = ctk.CTkEntry(frame, placeholder_text='Informe o título', font=('Meera', 18), width=300, height=50)
        self.entry_titulo_antigo.pack()
        
        label_titulo_novo = ctk.CTkLabel(frame, text='Título novo', font=('Ubuntu', 17))
        label_titulo_novo.pack(pady=50)
        self.entry_titulo_novo = ctk.CTkEntry(frame, placeholder_text='Informe o título', font=('Meera', 18), width=300, height=50)
        self.entry_titulo_novo.pack()
        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=lambda: self.editar_titulo2(email))
        botao_confirmar.pack(pady=30)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.tela_editar_tarefa(email))
        botao_voltar.pack(pady=30)
        self.label_retorno = ctk.CTkLabel(frame, text='')
        self.label_retorno.pack(pady=10)
        self.trocar_tela(frame)

    def editar_titulo2(self, email):
        tarefa = Tarefas(email)
        titulo_novo = self.entry_titulo_novo.get()
        titulo_antigo = self.entry_titulo_antigo.get()
        resultado = tarefa.editar_titulo(titulo_antigo, titulo_novo)
        if resultado:
            self.label_retorno.configure(text='Título trocado', text_color='green', font=('Meera', 20))
        else:
            self.label_retorno.configure(text='Título não encontrado', text_color='red', font=('Meera', 20))
            self.entry_titulo_antigo.delete(0, 'end')
            self.entry_titulo_novo.delete(0, 'end')

    def editar_descricao(self, email):
        frame = ctk.CTkFrame(self)
        label_descricao_antiga = ctk.CTkLabel(frame, text='Título da tarefa que deseja mudar', font=('Ubuntu', 17))
        label_descricao_antiga.pack(pady=50)
        self.entry_descricao_antiga = ctk.CTkEntry(frame, placeholder_text='Informe o título', font=('Meera', 18), width=300, height=50)
        self.entry_descricao_antiga.pack()
        
        label_descricao_nova = ctk.CTkLabel(frame, text='Descrição novo', font=('Ubuntu', 17))
        label_descricao_nova.pack(pady=50)
        self.entry_descricao_nova = ctk.CTkEntry(frame, placeholder_text='Informe o descrição', font=('Meera', 18), width=300, height=50)
        self.entry_descricao_nova.pack()
        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=lambda: self.editar_descricao2(email))
        botao_confirmar.pack(pady=30)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.tela_editar_tarefa(email))
        botao_voltar.pack(pady=30)
        self.label_retorno = ctk.CTkLabel(frame, text='')
        self.label_retorno.pack(pady=10)
        self.trocar_tela(frame)

    def editar_descricao2(self, email):
        tarefa = Tarefas(email)
        descricao_nova = self.entry_descricao_nova.get()
        descricao_antiga = self.entry_descricao_antiga.get()
        resultado = tarefa.editar_descricao(descricao_antiga, descricao_nova)
        if resultado:
            self.label_retorno.configure(text='Descrição modificada', text_color='green', font=('Meera', 20))
        else:
            self.label_retorno.configure(text='Título não encontrado', text_color='red', font=('Meera', 20))
            self.entry_descricao_antiga.delete(0, 'end')
            self.entry_descricao_nova.delete(0, 'end')

    def editar_prazo(self, email):
        frame = ctk.CTkFrame(self)
        label_prazo_antigo = ctk.CTkLabel(frame, text='Título da tarefa que deseja mudar', font=('Ubuntu', 17))
        label_prazo_antigo.pack(pady=50)
        self.entry_prazo_antigo = ctk.CTkEntry(frame, placeholder_text='Informe o título', font=('Meera', 18), width=300, height=50)
        self.entry_prazo_antigo.pack()
        
        label_prazo_novo = ctk.CTkLabel(frame, text='Prazo novo\n (seguindo o modelo do campo)', font=('Ubuntu', 17))
        label_prazo_novo.pack(pady=50)
        self.entry_prazo_novo = ctk.CTkEntry(frame, placeholder_text='DD/MM/AAAA', font=('Meera', 18), width=300, height=50)
        self.entry_prazo_novo.pack()
        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=lambda: self.editar_prazo2(email))
        botao_confirmar.pack(pady=30)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.tela_editar_tarefa(email))
        botao_voltar.pack(pady=30)
        self.label_retorno = ctk.CTkLabel(frame, text='')
        self.label_retorno.pack(pady=10)
        self.trocar_tela(frame)

    def editar_prazo2(self, email):
        tarefa = Tarefas(email)
        prazo_novo = self.entry_prazo_novo.get()
        prazo_antigo = self.entry_prazo_antigo.get()
        resultado = tarefa.editar_prazo(prazo_antigo, prazo_novo)
        if resultado == 0:
            self.label_retorno.configure(text='Formato inválido', text_color='red', font=('Meera', 20))
            self.entry_prazo_antigo.delete(0, 'end')
            self.entry_prazo_novo.delete(0, 'end')
        elif resultado == 1:
            self.label_retorno.configure(text='A data não pode ser anterior a hoje', text_color='red', font=('Meera', 20))
            self.entry_prazo_antigo.delete(0, 'end')
            self.entry_prazo_novo.delete(0, 'end')
        elif resultado == 2:
            self.label_retorno.configure(text='Prazo modificada', text_color='green', font=('Meera', 20))
        elif resultado == 3:
            self.label_retorno.configure(text='Título não encontrado', text_color='red', font=('Meera', 20))
            self.entry_prazo_antigo.delete(0, 'end')
            self.entry_prazo_novo.delete(0, 'end')

    def editar_prioridade(self, email):
        frame = ctk.CTkFrame(self)
        label_prioridade_antiga = ctk.CTkLabel(frame, text='Título da tarefa que deseja mudar', font=('Ubuntu', 17))
        label_prioridade_antiga.pack(pady=50)
        self.entry_prioridade_antiga = ctk.CTkEntry(frame, placeholder_text='Informe o título', font=('Meera', 18), width=300, height=50)
        self.entry_prioridade_antiga.pack()
        
        label_prioridade_nova = ctk.CTkLabel(frame, text='Prioridade nova\n (escrevendo uma das opções do campo)', font=('Ubuntu', 17))
        label_prioridade_nova.pack(pady=50)
        self.entry_prioridade_nova = ctk.CTkEntry(frame, placeholder_text='ALTA/ MEDIA/ BAIXA/ SEM PRIORIDADE', font=('Meera', 18), width=300, height=50)
        self.entry_prioridade_nova.pack()
        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=lambda: self.editar_prioridade2(email))
        botao_confirmar.pack(pady=30)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.tela_editar_tarefa(email))
        botao_voltar.pack(pady=30)
        self.label_retorno = ctk.CTkLabel(frame, text='')
        self.label_retorno.pack(pady=10)
        self.trocar_tela(frame)

    def editar_prioridade2(self, email):
        tarefa = Tarefas(email)
        prioridade_nova = self.entry_prioridade_nova.get()
        prioridade_antiga = self.entry_prioridade_antiga.get()
        resultado = tarefa.editar_prioridade(prioridade_antiga, prioridade_nova)
        if resultado:
            self.label_retorno.configure(text='Prioridade modificada', text_color='green', font=('Meera', 20))
        else:
            self.label_retorno.configure(text='Título não encontrado ou Prioridade inválida', text_color='red', font=('Meera', 20))
            self.entry_prioridade_antiga.delete(0, 'end')
            self.entry_prioridade_nova.delete(0, 'end')
    
    def apagar_tarefa(self, email):
        frame = ctk.CTkFrame(self)
        label_titulo_tarefa = ctk.CTkLabel(frame, text='Título da tarefa que deseja apagar', font=('Ubuntu', 17))
        label_titulo_tarefa.pack(pady=50)
        self.entry_titulo_tarefa = ctk.CTkEntry(frame, placeholder_text='Informe o título', font=('Meera', 18), width=300, height=50)
        self.entry_titulo_tarefa.pack()
        
        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=lambda: self.apagar_tarefa2(email))
        botao_confirmar.pack(pady=30)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.tela_editar_tarefa(email))
        botao_voltar.pack(pady=30)
        self.label_retorno = ctk.CTkLabel(frame, text='')
        self.label_retorno.pack(pady=10)
        self.trocar_tela(frame)

    def apagar_tarefa2(self, email):
        tarefa = Tarefas(email)
        titulo = self.entry_titulo_tarefa.get()
        resultado = tarefa.apagar_tarefa(titulo)
        if resultado:
            self.label_retorno.configure(text='Tarefa apagada', text_color='green', font=('Meera', 20))
        else:
            self.label_retorno.configure(text='Título não encontrado', text_color='red', font=('Meera', 20))
            self.entry_titulo_tarefa.delete(0, 'end')

    def organizar_cronograma(self, email):
        frame = ctk.CTkFrame(self)
        label_cronograma = ctk.CTkLabel(frame, text='CRONOGRAMA', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_cronograma.pack(pady=30)
        botao_ver_crono = ctk.CTkButton(frame, text='VISUALIZAR CRONOGRAMA', font=('Roboto', 15),width=200, height=50, command=lambda: self.crono_de_estudo(email, 1))
        botao_ver_crono.pack(pady=20)

        botao_add_crono = ctk.CTkButton(frame, text='CRIAR CRONOGRAMA', font=('Roboto', 15), width=200, height=50, command=lambda: self.tela_criar_crono(email))
        botao_add_crono.pack(pady=20)

        botao_add_crono = ctk.CTkButton(frame, text='VOLTAR', font=('Roboto', 15), width=200, height=50, command=lambda: self.menu_pais(email))
        botao_add_crono.pack(pady=20)
        self.trocar_tela(frame)

    def tela_criar_crono(self, email):
        frame = ctk.CTkFrame(self)
        label_cronograma = ctk.CTkLabel(frame, text='CRONOGRAMA - CRIAÇÃO\nINSIRA ABAIXO AS DISCIPLINAS ESTUDADAS EM CADA DIA', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_cronograma.pack(pady=15)

        frame_segunda = ctk.CTkFrame(frame, fg_color='transparent')
        frame_segunda.pack(pady=10)
        label_segunda = ctk.CTkLabel(frame_segunda, text='Segunda-Feira:', font=('Roboto', 17), width=150, height=50)
        label_segunda.pack(padx=10, side='left')
        self.entry_segunda = ctk.CTkEntry(frame_segunda, placeholder_text='Insira a matéria a ser estudada', font=('Meera', 15), width=300, height=50)
        self.entry_segunda.pack(padx=10, side='right')

        frame_terca = ctk.CTkFrame(frame, fg_color='transparent')
        frame_terca.pack(pady=10)
        label_terca = ctk.CTkLabel(frame_terca, text='Terça-Feira:', font=('Roboto', 17), width=150, height=50)
        label_terca.pack(padx=10, side='left')
        self.entry_terca = ctk.CTkEntry(frame_terca, placeholder_text='Insira a matéria a ser estudada', font=('Meera', 15), width=300, height=50)
        self.entry_terca.pack(padx=10, side='right')

        frame_quarta = ctk.CTkFrame(frame, fg_color='transparent')
        frame_quarta.pack(pady=10)
        label_quarta = ctk.CTkLabel(frame_quarta, text='Quarta-Feira:', font=('Roboto', 17), width=150, height=50)
        label_quarta.pack(padx=10, side='left')
        self.entry_quarta = ctk.CTkEntry(frame_quarta, placeholder_text='Insira a matéria a ser estudada', font=('Meera', 15), width=300, height=50)
        self.entry_quarta.pack(padx=10, side='right')

        frame_quinta = ctk.CTkFrame(frame, fg_color='transparent')
        frame_quinta.pack(pady=10)
        label_quinta = ctk.CTkLabel(frame_quinta, text='Quinta-Feira:', font=('Roboto', 17), width=150, height=50)
        label_quinta.pack(padx=10, side='left')
        self.entry_quinta = ctk.CTkEntry(frame_quinta, placeholder_text='Insira a matéria a ser estudada', font=('Meera', 15), width=300, height=50)
        self.entry_quinta.pack(padx=10, side='right')

        frame_sexta = ctk.CTkFrame(frame, fg_color='transparent')
        frame_sexta.pack(pady=10)
        label_sexta = ctk.CTkLabel(frame_sexta, text='Sexta-Feira:', font=('Roboto', 17), width=150, height=50)
        label_sexta.pack(padx=10, side='left')
        self.entry_sexta = ctk.CTkEntry(frame_sexta, placeholder_text='Insira a matéria a ser estudada', font=('Meera', 15), width=300, height=50)
        self.entry_sexta.pack(padx=10, side='right')
        
        frame_sabado = ctk.CTkFrame(frame, fg_color='transparent')
        frame_sabado.pack(pady=10)
        label_sabado = ctk.CTkLabel(frame_sabado, text='Sabado:', font=('Roboto', 17), width=150, height=50)
        label_sabado.pack(padx=10, side='left')
        self.entry_sabado = ctk.CTkEntry(frame_sabado, placeholder_text='Insira a matéria a ser estudada', font=('Meera', 15), width=300, height=50)
        self.entry_sabado.pack(padx=10, side='right')

        frame_domingo = ctk.CTkFrame(frame, fg_color='transparent')
        frame_domingo.pack(pady=10)
        label_domingo = ctk.CTkLabel(frame_domingo, text='Domingo:', font=('Roboto', 17),width=150, height=50)
        label_domingo.pack(padx=10, side='left')
        self.entry_domingo = ctk.CTkEntry(frame_domingo, placeholder_text='Insira a matéria a ser estudada', font=('Meera', 15), width=300, height=50)
        self.entry_domingo.pack(padx=10, side='right')

        frame_botoes = ctk.CTkFrame(frame, fg_color='transparent')
        frame_botoes.pack(pady=10)
        botao_criar = ctk.CTkButton(frame_botoes, text='CRIAR CRONOGRAMA', font=('Roboto', 15), width=200, height=50, command=lambda: self.criar_crono(email))
        botao_criar.pack(side='left', padx=10)

        botao_voltar = ctk.CTkButton(frame_botoes, text='VOLTAR', font=('Roboto', 15), width=200, height=50, command=lambda: self.organizar_cronograma(email))
        botao_voltar.pack(side='right', padx=10)
        self.label_campo_vazio = ctk.CTkLabel(frame, text='')
        self.label_campo_vazio.pack(pady=10)
        self.trocar_tela(frame)
        
    def criar_crono(self, email):
        cronograma = Cronograma(email)
        lista_cronograma = [self.entry_segunda.get(), self.entry_terca.get(), self.entry_quarta.get(),
                            self.entry_quinta.get(), self.entry_sexta.get(), self.entry_sabado.get(), self.entry_domingo.get()]
        if '' in lista_cronograma or ' ' in lista_cronograma:
            self.label_campo_vazio.configure(text='Campo vazio', text_color='red', font=('Meera', 20))
        else:
            cronograma.add_cronograma(lista_cronograma)
            self.crono_de_estudo(email, 1)

    def editar_notas(self, email):
        frame = ctk.CTkFrame(self)
        label_notas = ctk.CTkLabel(frame, text='NOTAS - EDIÇÃO', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_notas.pack(pady=20)
        self.tabela_notas(email, frame)
        label_disciplina = ctk.CTkLabel(frame, text='DISCIPLINA', font=('Ubuntu', 20),
                                         width=1280, height=30, bg_color='transparent', text_color='#f5f7fa')
        label_disciplina.pack(pady=5)
        self.entry_disciplina = ctk.CTkEntry(frame, placeholder_text='Insira o índice da disciplina', font=('Meera', 15), width=300, height=50)
        self.entry_disciplina.pack(pady=10)
        frame_botoes = ctk.CTkFrame(frame, fg_color='transparent')
        frame_botoes.pack(pady=20)
        botao_nota1 = ctk.CTkButton(frame_botoes, text='Nota 1', font=('Roboto', 15), width=200, height=50, command=lambda: self.campo_vazio(email, 1))
        botao_nota1.pack(padx=10, side='left')
        botao_nota2 = ctk.CTkButton(frame_botoes, text='Nota 2', font=('Roboto', 15), width=200, height=50, command=lambda: self.campo_vazio(email, 2))
        botao_nota2.pack(padx=10, side='right')
        botao_voltar = ctk.CTkButton(frame, text='VOLTAR', font=('Roboto', 15), width=200, height=50, command=lambda: self.menu_pais(email))
        botao_voltar.pack()
        self.label_disciplina_vazio = ctk.CTkLabel(frame, text='')
        self.label_disciplina_vazio.pack(pady=10)
        self.trocar_tela(frame)

    def campo_vazio(self, email, contador):
        indice_disciplina = self.entry_disciplina.get()
        if indice_disciplina == '' or indice_disciplina == ' ':
            self.label_disciplina_vazio.configure(text='Campo vazio', text_color='red', font=('Meera', 20))
        elif indice_disciplina not in ['1','2','3','4','5','6','7','8','9','10']:
            self.label_disciplina_vazio.configure(text='Dígito inválido', text_color='red', font=('Meera', 20))
            self.entry_disciplina.delete(0, 'end')
        else:
            if contador == 1:
                self.editar_nota1(email, indice_disciplina)
            elif contador == 2:
                self.editar_nota2(email, indice_disciplina)
            
    def editar_nota1(self, email, disciplina):
        frame = ctk.CTkFrame(self)
        frame_nota = ctk.CTkFrame(frame, fg_color='transparent')
        frame_nota.pack(pady=20)
        label_nota1 = ctk.CTkLabel(frame_nota, text='Nota 1:', font=('Roboto', 17),width=150, height=50)
        label_nota1.pack(padx=10, side='left')
        self.entry_nota1 = ctk.CTkEntry(frame_nota, placeholder_text='Insira a nota', font=('Meera', 15), width=300, height=50)
        self.entry_nota1.pack(padx=10, side='right')
        botao_nota1 = ctk.CTkButton(frame, text='ALTERAR', width=200, height=50, command=lambda: self.alterar_nota1(email, disciplina))
        botao_nota1.pack(pady=10)
        self.label_nota_vazio = ctk.CTkLabel(frame, text='')
        self.label_nota_vazio.pack(pady=10)
        self.trocar_tela(frame)

    def editar_nota2(self, email, disciplina):
        frame = ctk.CTkFrame(self)
        frame_nota = ctk.CTkFrame(frame, fg_color='transparent')
        frame_nota.pack(pady=20)
        label_nota2 = ctk.CTkLabel(frame_nota, text='Nota 2:', font=('Roboto', 17),width=150, height=50)
        label_nota2.pack(padx=10, side='left')
        self.entry_nota2 = ctk.CTkEntry(frame_nota, placeholder_text='Insira a nota', font=('Meera', 15), width=300, height=50)
        self.entry_nota2.pack(padx=10, side='right')
        botao_nota2 = ctk.CTkButton(frame, text='ALTERAR', width=200, height=50, command=lambda: self.alterar_nota2(email, disciplina))
        botao_nota2.pack(pady=10)
        self.label_nota_vazio = ctk.CTkLabel(frame, text='')
        self.label_nota_vazio.pack(pady=10)
        self.trocar_tela(frame)

    def alterar_nota1(self, email, disciplina):
        notas = Notas(email)
        indice_disciplina = disciplina
        nota_alterada = self.entry_nota1.get()
        erros = []
        resultado = notas.editar_nota1(nota_alterada, indice_disciplina)
        if resultado == 0:
            self.label_nota_vazio.configure(text='Campo vazio', text_color='red', font=('Meera', 20))
        elif resultado == 1:
            erros.append('Não é permitido letras')
            self.label_nota_vazio.configure(text='Contém letras', text_color='red', font=('Meera', 20))
            self.entry_nota1.delete(0, 'end')
        elif resultado == 2:
            self.editar_notas(email)
        
    def alterar_nota2(self, email, disciplina):
        notas = Notas(email)
        indice_disciplina = disciplina
        nota_alterada = self.entry_nota2.get()
        erros = []
        resultado = notas.editar_nota2(nota_alterada, indice_disciplina)
        if resultado == 0:
            self.label_nota_vazio.configure(text='Campo vazio', text_color='red', font=('Meera', 20))
        elif resultado == 1:
            erros.append('Não é permitido letras')
            self.label_nota_vazio.configure(text='Contém letras', text_color='red', font=('Meera', 20))
            self.entry_nota2.delete(0, 'end')
        elif resultado == 2:
            self.editar_notas(email)

    def tela_add_lembrete(self, email):
        frame = ctk.CTkFrame(self)
        label_lembrete = ctk.CTkLabel(frame, text='LEMBRETES - CRIAÇÃO', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_lembrete.pack(pady=20)

        label_titulo_lembrete = ctk.CTkLabel(frame, text='Título do Lembrete:', font=('Roboto', 15))
        label_titulo_lembrete.pack(pady=10)
        self.entry_titulo_lembrete = ctk.CTkEntry(frame, placeholder_text='Informe um título', width=300, height=50, font=('Meera', 20))
        self.entry_titulo_lembrete.pack(pady=10)

        label_descricao_lembrete = ctk.CTkLabel(frame, text='Descrição do Lembrete:', font=('Roboto', 15))
        label_descricao_lembrete.pack(pady=10)
        self.entry_descricao_lembrete = ctk.CTkEntry(frame, placeholder_text='Informe uma descrição', width=300, height=50, font=('Meera', 20))
        self.entry_descricao_lembrete.pack(pady=10)

        botao_criar_lembrete = ctk.CTkButton(frame, text='CRIAR', font=('Roboto', 20), width=200, height=50, command=lambda: self.add_lembrete(email))
        botao_criar_lembrete.pack(pady=20)
        botao_voltar = ctk.CTkButton(frame, text='VOLTAR', font=('Roboto', 20), width=200, height=50, command=lambda: self.menu_pais(email))
        botao_voltar.pack(pady=20)
        self.label_lembrete_erro = ctk.CTkLabel(frame, text='')
        self.label_lembrete_erro.pack(pady=10)
        self.trocar_tela(frame)

    def add_lembrete(self, email):
        titulo = self.entry_titulo_lembrete.get()
        descricao = self.entry_descricao_lembrete.get()
        if titulo == '' or titulo == ' ':
            self.label_lembrete_erro.configure(text='Campo vazio', text_color='red', font=('Meera', 20))
            self.entry_titulo_lembrete.delete(0, 'end')
        elif descricao == '' or descricao == ' ':
            self.label_lembrete_erro.configure(text='Campo vazio', text_color='red', font=('Meera', 20))
            self.entry_descricao_lembrete.delete(0, 'end')
        else:
            lembrete = Lembrete(email)
            lembrete.add_lembretes(titulo, descricao)
            self.label_lembrete_erro.configure(text='Lembrete Criado', text_color='green', font=('Meera', 20))

    def editar_perfil(self, email):
        frame = ctk.CTkFrame(self)
        label_menu_editar_perfil = ctk.CTkLabel(frame, text='EDITAR PERFIL', font=(
            'Ubuntu', 20), width=650, height=50)
        label_menu_editar_perfil.pack(pady=18)
        botao_editar_email = ctk.CTkButton(frame, width=200, height=50, text='EDITAR EMAIL', font=(
            'Roboto', 15), command=lambda: self.tela_editar_email(email))
        botao_editar_email.pack(pady=10)

        botao_editar_nome = ctk.CTkButton(frame, width=200, height=50, text='EDITAR NOME', font=(
            'Roboto', 15), command=lambda: self.tela_editar_nome(email))
        botao_editar_nome.pack(pady=10)

        botao_editar_senha = ctk.CTkButton(frame, width=200, height=50, text='EDITAR SENHA', font=(
            'Roboto', 15), command=lambda: self.tela_editar_senha(email))
        botao_editar_senha.pack(pady=10)

        botao_editar_serie = ctk.CTkButton(frame, width=200, height=50, text='EDITAR SÉRIE', font=(
            'Roboto', 15), command=lambda: self.tela_editar_serie(email))
        botao_editar_serie.pack(pady=10)

        botao_apagar_perfil = ctk.CTkButton(frame, width=200, height=50, text='APAGAR PERFIL', font=(
            'Roboto', 15), command=lambda: self.excluir_perfil(email))
        botao_apagar_perfil.pack(pady=10)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.menu_principal(email))
        botao_voltar.pack(pady=10)
        self.trocar_tela(frame)

    def tela_editar_email(self, email):
        frame = ctk.CTkFrame(self)
        label_email = ctk.CTkLabel(frame, text='EDITANDO EMAIL', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_email.pack(pady=20)

        label_email_antigo = ctk.CTkLabel(frame, text='Email atual:', font=('Roboto', 15))
        label_email_antigo.pack(pady=10)
        self.entry_email_antigo = ctk.CTkEntry(frame, placeholder_text='Informe o novo atual', width=300, height=50, font=('Meera', 20))
        self.entry_email_antigo.pack(pady=10)

        label_email_novo = ctk.CTkLabel(frame, text='Email novo:', font=('Roboto', 15))
        label_email_novo.pack(pady=10)
        self.entry_email_novo = ctk.CTkEntry(frame, placeholder_text='Informe o novo email', width=300, height=50, font=('Meera', 20))
        self.entry_email_novo.pack(pady=10)

        botao_mudar_email = ctk.CTkButton(frame, text='MUDAR', font=('Roboto', 20), width=200, height=50, command=lambda: self.editar_email(email))
        botao_mudar_email.pack(pady=20)
        botao_voltar = ctk.CTkButton(frame, text='VOLTAR', font=('Roboto', 20), width=200, height=50, command=lambda: self.menu_principal(email))
        botao_voltar.pack(pady=20)
        self.label_email_erro = ctk.CTkLabel(frame, text='')
        self.label_email_erro.pack(pady=10)
        self.trocar_tela(frame)

    def editar_email(self, email):
        usuario_email_antigo = Usuario(email=self.entry_email_antigo.get())
        usuario_email_novo = Usuario(email=self.entry_email_novo.get())
        erros = []
        resultado_email_antigo = usuario_email_antigo.validar_email()
        resultado_email_novo = usuario_email_novo.validar_email()
        if resultado_email_novo == 1:
            erros.append('Email já cadastrado, insira um email novo')
        elif resultado_email_antigo == 2 or resultado_email_novo == 2:
            erros.append('Email inválido, insira um email válido')
            
        if erros:
            self.label_email_erro.configure(text='\n'.join(
                erros), text_color='red', font=('Meera', 20))
            self.entry_email_novo.delete(0, 'end')
            self.entry_email_antigo.delete(0, 'end')
        else:
            usuario_email_antigo.mudar_email(self.entry_email_novo.get())
            self.label_email_erro.configure(text='Emal validado. Reiniciando', 
                                            text_color='green', font=('Meera', 20))
            sleep(1)
            self.login()
    
    def tela_editar_nome(self, email):
        frame = ctk.CTkFrame(self)
        label_nome = ctk.CTkLabel(frame, text='EDITANDO NOME', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_nome.pack(pady=20)

        label_nome_novo = ctk.CTkLabel(frame, text='Novo nome:', font=('Roboto', 15))
        label_nome_novo.pack(pady=10)
        self.entry_nome_novo = ctk.CTkEntry(frame, placeholder_text='Informe o novo nome', width=300, height=50, font=('Meera', 20))
        self.entry_nome_novo.pack(pady=10)
        botao_trocar = ctk.CTkButton(frame, text='MUDAR', font=('Roboto', 20), width=200, height=50, command=lambda: self.editar_nome(email))
        botao_trocar.pack(pady=20)

        botao_voltar = ctk.CTkButton(frame, text='VOLTAR', font=('Roboto', 20), width=200, height=50, command=lambda: self.menu_principal(email))
        botao_voltar.pack(pady=20)
        self.label_nome_erro = ctk.CTkLabel(frame, text='')
        self.label_nome_erro.pack(pady=10)
        self.trocar_tela(frame)

    def editar_nome(self, email):
        usuario = Usuario(nome=self.entry_nome_novo.get(), email=email)
        erros = []
        resultado_nome = usuario.validar_nome()
        if not resultado_nome:
            erros.append('Nome de usuário incorreto')
            self.campo_nome.delete(0, 'end')
        usuario.mudar_nome(self.entry_nome_novo.get())       
        if erros:
            self.label_nome_erro.configure(text='\n'.join(
                erros), text_color='red', font=('Meera', 20))
            self.entry_email_novo.delete(0, 'end')
        else:
            sleep(0.45)
            self.menu_principal(email)

    def tela_editar_senha(self, email):
        self.var_senha = ctk.BooleanVar(value=False)
        self.var_confirma_senha = ctk.BooleanVar(value=False)
        frame = ctk.CTkFrame(self)
        label_nome_senha = ctk.CTkLabel(frame, text='EDITANDO SENHA', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_nome_senha.pack(pady=20)

        label_senha = ctk.CTkLabel(frame, text='NOVA SENHA', font=(
            'Roboto', 15), width=400, height=60)
        label_senha.pack()
        self.campo_senha = ctk.CTkEntry(
            frame, show="*", placeholder_text='Digite sua senha min.: 8 caracteres', font=('Meera', 18), width=300, height=50)
        self.campo_senha.pack(pady=10)
        check_senha = ctk.CTkCheckBox(
            frame, text='Exibir senha', variable=self.var_senha, command=self.mostrar_senha)
        check_senha.pack(pady=10)
        label_confirma_senha = ctk.CTkLabel(
            frame, text='CONFIRME SUA SENHA', font=('Roboto', 15), width=400, height=60)
        label_confirma_senha.pack()
        self.campo_confirma_senha = ctk.CTkEntry(
            frame, show='*', placeholder_text='Confirme sua senha', font=('Meera', 20), width=300, height=50)
        self.campo_confirma_senha.pack(pady=15)
        check_senha = ctk.CTkCheckBox(frame, text='Exibir senha',
                                      variable=self.var_confirma_senha, command=self.mostrar_senha_confirmada)
        check_senha.pack(pady=10)

        botao_confirmar = ctk.CTkButton(frame, width=200, height=50, text='CONFIRMAR', font=(
            'Roboto', 15), command=lambda: self.editar_senha(email))
        botao_confirmar.pack(pady=20)

        botao_voltar = ctk.CTkButton(frame, width=200, height=50, text='VOLTAR', font=(
            'Roboto', 15), command=lambda: self.menu_principal(email))
        botao_voltar.pack()
        self.label_confirma = ctk.CTkLabel(frame, text='')
        self.label_confirma.pack(pady=10)
        self.trocar_tela(frame)

    def editar_senha(self, email):
        senha = self.campo_senha.get()
        confirma_senha = self.campo_confirma_senha.get()
        erros = []  
        usuario = Usuario(email=email)
        if senha == '':
            erros.append('Senha vazia, tente novamente')
            self.campo_senha.delete(0, 'end')
            self.campo_confirma_senha.delete(0, 'end')
        elif len(senha) < 8:
            erros.append('Senha muito curta, tente novamente')
            self.campo_senha.delete(0, 'end')
            self.campo_confirma_senha.delete(0, 'end')
        elif senha != confirma_senha:
            erros.append('Senhas diferentes, tente novaemnte')
            self.campo_senha.delete(0, 'end')
            self.campo_confirma_senha.delete(0, 'end')

        if erros:
            self.label_confirma.configure(text='\n'.join(erros), text_color='red', font=(
                'Meera', 20))  # Exibe as mensagens de erro
        else:
            self.label_confirma.configure(
                text='Senha Modificada', text_color='green', font=('Meera', 20))
            usuario.mudar_senha(senha)

    def tela_editar_serie(self, email):
        frame = ctk.CTkFrame(self)
        label_serie = ctk.CTkLabel(frame, text='EDITANDO SÉRIE', font=('Ubuntu', 20),
                                         width=1280, height=98, bg_color='#3a3b3c', text_color='#f5f7fa')
        label_serie.pack(pady=20)

        label_serie_novo = ctk.CTkLabel(frame, text='Nova séria:', font=('Roboto', 15))
        label_serie_novo.pack(pady=10)
        self.entry_serie_novo = ctk.CTkEntry(frame, placeholder_text='Informe a nova série', width=300, height=50, font=('Meera', 20))
        self.entry_serie_novo.pack(pady=10)
        botao_trocar = ctk.CTkButton(frame, text='MUDAR', font=('Roboto', 20), width=200, height=50, command=lambda: self.editar_serie(email))
        botao_trocar.pack(pady=20)

        botao_voltar = ctk.CTkButton(frame, text='VOLTAR', font=('Roboto', 20), width=200, height=50, command=lambda: self.menu_principal(email))
        botao_voltar.pack(pady=20)
        self.label_serie_erro = ctk.CTkLabel(frame, text='')
        self.label_serie_erro.pack(pady=10)
        self.trocar_tela(frame)

    def editar_serie(self, email):
        serie = Usuario(email=email, serie=self.entry_serie_novo.get())
        erros = []
        resultado = serie.validar_serie()
        if not resultado:
            erros.append('Série inválida! Informe uma série válida')
            self.entry_serie_novo.delete(0, 'end')

        if erros:
            self.label_serie_erro.configure(text='\n'.join(
                erros), text_color='red', font=('Meera', 20))
        else:
            serie.mudar_serie(self.entry_serie_novo.get())
            self.label_serie_erro.configure(
                text='Série alterada', text_color='green', font=('Meera', 20))
            
    def excluir_perfil(self, email):
        usuario = Usuario(email=email)
        usuario.apagar_perfil()
        sleep(0.3)
        self.login()

if __name__ == "__main__":
    app = App()
    app.mainloop()
