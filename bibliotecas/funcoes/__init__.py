from bibliotecas import interface
from bibliotecas import arquivo

def vercadastrados():
    interface.cabecalho('PESSOAS CADASTRADAS'.center(42))
    arquivo.ler_arquivo()

def cadastrarnovo(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, "at")
    except:
        print('\033[31mHouve um erro ao abrir o arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados!\033[m')
        else:
            print(f'\033[32m {nome} foi adcionado com sucesso.\033[m')
            a.close()
        


def sair():
    interface.cabecalho('SAINDO DO SISTEMA...ATÉ LOGO!'.center(42))

def leiaint(txt):
    inteiro = input(txt)

    while not inteiro.isnumeric():
        print('\033[31mERRO: DIGITE UM VALOR INTEIRO\033[m')
        inteiro = input(txt)

    if inteiro.isnumeric():
        inteiro = int(inteiro)

    return inteiro
