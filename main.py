from cadastro import cadastrar_usuario, carregar_dados, redefinir_senha

def tracinho():
    print('-'*40)
    
def menu_estudante():
    print('='*40)
    print(f"{'MENU'}.' '^40")
    print('='*40)

def verifica_email(email): 
    dados = carregar_dados()   
    if not email in dados:
        print('Email inválido! Cadastre um novo usuário ou insira um email válido.')
       
        while True:
            print('[1] Inserir um email válido')
            print('[2] Cadastrar um novo usuário')
            tracinho()
            escolha = int(input('Esolha uma opção acima: '))
            if  escolha == 1:
                email = str(input('Insira um email válido: '))
                verifica_email(email)
                break
            elif escolha == 2:
                cadastrar_usuario()
                break 
            elif escolha == None:
                print('Informe uma escolha válida')                                            
            else:
                print('Opção inválida! Tente novamente!')
            break

def verifica_senha(email, senha):
    dados = carregar_dados()
    contador = 0
    while contador < 4:
        if dados[email]['Senha'] == senha:
            menu_estudante()
            break
        else:
            print('Senha incorreta, tente novamente!')
            senha = str(input('Informe a sua senha: '))
            contador += 1
        if contador == 4:
            tracinho()
            print('Quantidade de tentativas expirada, crie uma nova senha!')
            tracinho()
            redefinir_senha(email)

def login():
    dados = carregar_dados()
    tracinho()
    print('[1] Login')
    print('[2] Cadastrar novo usuário')
    tracinho()
    while True:
        try:
            escolha = int(input('Escolha uma opção: '))
        except:
            print('Informe uma escolha válida')
        else:
            break

    while True:
        if escolha == 1:
            email = str(input('Informe o email de login: '))
            verifica_email(email)
            while True:
                tracinho()
                print('[1] Informe a senha')
                print('[2] Esqueceu a senha')
                tracinho()
                while True:
                    try:
                        escolha = int(input('Escolha uma opção: '))
                    except:
                        print('Informe uma escolha válida')
                    else:
                        break
                escolha = int(input('Esolha uma opção acima: '))
                if escolha == 1:
                    senha = str(input('Informe a sua senha: '))
                    tracinho()
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
            cadastrar_usuario()
            break
        else:
            print('Opção inválida! Tente novamente!')
login()

'''
Pensar em uma forma de criar uma função pra testar o erro de campo vazio
'''