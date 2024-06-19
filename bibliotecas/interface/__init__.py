def linha(tam=42):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())

def menu(a):
    lista = a

    cabecalho('MENU PRINCIPAL'.center(42))
    for indice, item in enumerate(lista):
        print(f'\033[33m{indice+1} -\033[m \033[36m{item}\033[m')
    print(linha())

    