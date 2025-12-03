# Ninho Desk 🦉

**Repositório Ninho Desk - Projetos Interdiciplinares de Sistemas da Informação 1 (PISI1)**  
<br/>Desenvolvido por: [Lucas Menezes](https://github.com/lucasmenezes255) e [Bruno Fellype](https://github.com/BrunoFellype)  
Orientado por: [Cleyton Magalhães](https://github.com/cvanut)  
<br/>Um app de gerenciamento de tarefas acadêmico voltado especialmente para estudantes do Ensino Fundamental com suporte e controle dos pais nas atividades e rotina dos filhos. O app é voltado principalmente para uso acadêmico, porém é de livre escolha utilizá-lo também como gerenciador de tarefas comuns das crianças.

## Prazos de Entrega
- [x] 1ªVA 15/10/2025 (release)
- [x] 2ºVA 03/12/2025 (release)
- [ ] 3ªVA 10/12/2025 (release)

## Requisitos funcionais
### <ins>1ª Release
#### **RF001** Cadastro do usuário  
- Adicionar dados de Usuário
- Realizar validações de dados
#### **RF002** Tela de Login  
- Verificação de cadastro
- Esqueceu senha
- Validação de dados
#### **RF003** Menu do estudante  
- Redirecionamento para funcionalidades
#### **RF004** Conferir Tarefas  
- Visualizar tarefas selecionadas
#### **RF005** Ver Cronograma  
- Visualizar o cronograma definido pelos pais
#### **RF006** Tela de Lembrete  
- Adicionar lembrete
- Visualizar lembretes
#### **RF007** Tela de Controle dos Pais  
- Senha mestre
- Redirecionamento a partir de sub-menu
#### **RF008** Criação da Senha Mestre  
- Esqueceu a senha mestre
- Validação de senha mestre
#### **RF009** Administrar Tarefas  
- Criar tarefas
- Editar tarefas
- Definir prioridade
#### **RF010** Organizar Cronograma  
- Criar cronograma
- Visualizar cronograma existente
#### **RF011** Criar Lembretes  
- Adicionar título de lembrete
- Adicionar descrição de lembrete

### <ins>2ª Release
#### **RF012** Sistema de Notas
- Adicionar notas
- Visualizar grade de notas
#### **RF013** Agrupamento de Tarefas  
- Divisão de tarefas por conclusão ou pendência
- Divisão de tarefas por grua de prioridade
#### **RF014** Interface Gráfica
- Interface responsiva contendo todos os outros requisitos

## Descrição de módulos

`main.py`: contém o loop principal da interface gráfica.  
`cadastro.py`: armazena a Classe Usuario e seus respectivos métodos.  
`cronograma.py`: armazena a Classe Cronograma e seus respectivos métodos.  
`lembretes.py`: armazena a Classe Lembrete e seus respectivos métodos.  
`notas.py`: armazena a Classe Notas e seus respectivos métodos.  
`tarefas.py`: armazena a Classe Tarefas e seus respectivos métodos.  
`verificacoes.py`: armazena a Classe Verificacao e seus respectivos métodos.  

## TECNOLOGIAS UTILIZADAS

| Tecnologias         | Utilidade |
|---------------------|-----------|
| Python 3.13.7|Linguagem principal de desenvolvimento do sistema|
| Trello|Organização e gerenciamento de tarefas e fluxos do projeto|
| Git, GitHub, GitHub Desktop|Controle de versão, hospedagem do repositório e interface visual para commits e sincronização|
| Draw.io|Design de fluxogramas|

## Bibliotecas utilizadas

|Biblioteca| Descrição|  
|----------|----------|
|os|Para lidar com arquivos json e para limpar terminal|
|json|Lib necessária para lidar com os arquivos json|
|rich (1ªRelease)|Usada para criação das tabelas de exibição da quantidade de tarefas por prioridade|
|re|Usada para criar expressões modelo para verificação de email e de data|
|datetime|Usado para criação de prazos|
|maskpass (1ªRelease)|Mascarar dígitos de entrada do terminal. Útil para criação de senhas|
|time|Usada para controlar o tempo entre a execução de um comando e outro|
|tkinter (2ªRelease)|Usada para adicionar a interface gráfica|
|customtkinter (2ªRelease)|Usada para adicionar personalizações e melhorias na interface|

## Instalações necessárias
```
pip install maskpass
pip install rich
pip install customtkinter
```

## Algumas imagens do projeto

#### <ins>**Tela de Início:** <br>
<br>![início](imagens/ninho%20desk%20inicio.png)
#### <ins>**Tela de Login:** <br>
<br>![login](imagens/ninho%20desk%20login.png)
#### <ins>**Tela do Menu do Estudante:** <br>
<br>![estudante](imagens/ninho%20desk%20menu%20estudante.png)
#### <ins>**Tela do Menu dos Pais:** <br>
<br>![pais](imagens/ninho%20desk%20menu%20pais.png)

## Fluxograma do projeto
Tenha uma visão do fluxograma utilizado, clicando [aqui](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Fluxogramas-NinhoDesk-1RELEASE.drawio&dark=auto&authuser=0#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1TRWJ4s5_qd_LGb-PHgRMw5D1oG5QvwkV%26export%3Ddownload).
