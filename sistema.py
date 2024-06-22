#pacotes e funções importadas
from bibliotecas import interface
from bibliotecas import funcoes
from bibliotecas import arquivo
from time import sleep

#chamando o arquivo criado

arquivo.criacao_do_arquivo()

arq = "sistema_menu.txt"

#Loop para fazer o sistema ficar ativo até que o usuário deseja finaliza-lo

while True:

    #Lista das informações que existem no menu 

    interface.menu(['Ver cadastrados', 'Cadastrar novo', 'Sair do sistema'])

    #Variável para escolher uma opção

    decisao = funcoes.leiaint('\033[33mSua escolha:\033[m ')

    #verificação de inteiros diferentes das opções do menu

    while decisao < 1 or decisao > 3:
        print('\033[31mERRO: DIGITE UM INTEIRO VÁLIDO\033[m')
        decisao = funcoes.leiaint('\033[33mSua escolha:\033[m ')

    #verificação da opção digitada
    
    if decisao == 3:
        funcoes.sair()
        break
    else:
        if decisao == 1:
            funcoes.vercadastrados()
        elif decisao == 2:
            interface.cabecalho('CADASTRAR NOVO'.center(42))
            nome = str(input('Nome: '))
            idade = str(input('Idade: '))
            funcoes.cadastrarnovo(arq, nome, idade)

    sleep(1)
