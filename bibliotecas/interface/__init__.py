# função para mostrar linhas no terminal, para facilitar a leitura do usuário
def linha(tam=42):
    return '-'*tam

# função usada para exibir o cabeçalho da ação que está sendo executada.

def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())

# função para exibição do menu de opções

def menu(a):
    lista = a

    cabecalho('MENU PRINCIPAL'.center(42))
    for indice, item in enumerate(lista):
        print(f'\033[33m{indice+1} -\033[m \033[36m{item}\033[m')
    print(linha())

    