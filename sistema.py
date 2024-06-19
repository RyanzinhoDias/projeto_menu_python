from bibliotecas import interface
from bibliotecas import funcoes
from bibliotecas import arquivo
from time import sleep

arquivo.criacao_do_arquivo()

arq = "sistema_menu.txt"

while True:
    interface.menu(['Ver cadastrados', 'Cadastrar novo', 'Sair do sistema'])
    decisao = funcoes.leiaint('\033[33mSua escolha:\033[m ')

    while decisao < 1 or decisao > 3:
        print('\033[31mERRO: DIGITE UM INTEIRO VÁLIDO\033[m')
        decisao = funcoes.leiaint('\033[33mSua escolha:\033[m ')

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
