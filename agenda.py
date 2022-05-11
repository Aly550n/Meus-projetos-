# Meus-projetos-
Meus projetos de iniciante
def menu():
    opcao= input('''
    ==================================================================
                         PROJETO AGENDA EM PYTHON
    MENU:
    [1]CADASTRAR CONTATO
    [2]LISTAR CONTATO
    [3]DELETAR CONTATO
    [4]BUSCAR CONTATO PELO NOME
    [5]SAIR
    ==================================================================
    ESCOLHA UMA OPÇAO A CIMA: ''')
    if opcao == "1":
        cadastrarcontato()
    elif opcao == "2":
        listarcontato()
    elif opcao == "3":
        deletarcontato()
    elif opcao == "4":
        buscarcontatopenome()
    else:
        sair()

def cadastrarcontato():
    idContato = input('Escolha o ID do seu contato: ')
    nome = input('Escreva o nome do seu contato: ')
    telefone = input('Escreva o telefone do seu contato: ')
    email = input('Escreva o email do contato: ')
    try:
        agenda = open('agenda.txt','a')
        dados = f'{idContato};{nome};{telefone};{email}\n'
        agenda.write(dados)
        agenda.close()
        print(f'contato gravado com sucesso!!!')
    except:
        print('ERRO na gravacao do contato!')

def listarcontato():
    agenda = open('agenda.txt','r')
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarcontato():
    nomedeletado = input('Digite o nome que e para ser deletado: ')
    agenda = open('agenda.txt','r')
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomedeletado not in aux[i]:
            aux2.append(aux[i])
        agenda = open('agenda.txt','w')
        for i in aux2:
            agenda.write(i)
        print(f'Contato deletado com sucesso!')
        listarcontato()

def buscarcontatopenome():
    nome=input(f'Digite o nome a ser procurado: ')
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        if nome in contato.split(';')[1]:
            print(contato)
    agenda.close()

def sair():
    print(f'Ate mais! S2')
    exit()

def main():
    menu()
main()
