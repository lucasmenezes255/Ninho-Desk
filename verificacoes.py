from cadastro import carregar_dados, Usuario

class Verificacao(Usuario):
    def __init__(self, email, senha='', confirma_senha=''):
        self.email = email
        self.senha = senha
        self.confirma_senha = confirma_senha
    def __repr__(self):
        return f"{self.email}"
     
    def verifica_email_login(self):
        dados = carregar_dados()
        if self.email not in dados:
            return False
        else:
            return True

    def verificar_senha(self):
        dados = carregar_dados()
        if dados[self.email]['Senha'] == self.senha:
            return True
        else:
            return False

    def verificar_senha_master(self):
        dados = carregar_dados()
        if dados[self.email]['Senha Mestre'] == self.senha and self.senha == self.confirma_senha:
            return 0
        else:
            if self.senha != self.confirma_senha:
                return 1
            else:
                return 2
        