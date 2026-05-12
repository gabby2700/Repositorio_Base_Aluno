from os import system

def limpa_tela():
    system("cls")

def adicionar_nome(Lista_nomes, nome) :
    Lista_nomes.append(nome)

def remover_nome(Lista_nome,nome):
    Lista_nome.remove(nome)

def mostrar_nomes(Lista_nomes):
        for nome in Lista_nomes:
            print(nome)
nomes =[]
while True:
    limpa_tela( )
    menu = input("Escollha sua opção :\n [1] -Listar nomes \n[2] - Adicionar nomes\n[3] - Remover nomes\n[0] - Sair \n Sua opção \n ")
    if menu == "0" :
        break
    elif menu == "1":
        mostrar_nomes(nomes)
        input("Aperte Enter para continuar")
    elif menu =="2" :
         nome_salvar = input("Digite o nome que deseja adicionar :")
         remover_nome(nomes, remover_nome)
    else:
        print("Opção inválida")
        input("Aperte Enter para continuar")