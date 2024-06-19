def criacao_do_arquivo():
    try:
        arquivo = open("sistema_menu.txt", "r")
    except FileNotFoundError:
        arquivo = open("sistema_menu.txt", "w")
        print('Arquivo sistema_menu.txt criado com sucesso')
    finally:
        arquivo.close()


def ler_arquivo():
    with open("sistema_menu.txt", "r") as arquivo:
        texto = arquivo.readlines()
        for linha in texto:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')


