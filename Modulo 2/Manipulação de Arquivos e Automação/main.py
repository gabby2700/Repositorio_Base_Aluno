import csv
import os

def limpar_tela():
    os.system("cls")

print("Seja bem-vindo ao sistema de Notas 😺")

while True :
    opcao = input("[1] - Cadastrar aluno e nota\n " \
    "[2]  - Listar alunos\n "\
    "[3]  - Lisar alunos com nota acima de 8\n " \
    "[0]  - Sair\nSua opção: ")     


    if opcao == "1" :
        nome = input("Digite o nome do(a):")
        idade = int(input("Digite a idade do (a) :" ))
        nota = float(input("Digite a nota do (a) : " ))
        with open("alunos.csv","a",newline = "") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([nome,idade,nota])

    elif opcao == "2" :
        with open ("alunos.csv","r") as arquivo :
            leitor = csv.reader(arquivo)
            for linha in leitor :
                nome,idade,nota = linha
                print(f"{nome.strip():^15} | {idade.strip():^10} | {nota.strip():^10}")

    elif opcao == "3" :
        with open ("alunos.csv","r") as arquivo :
            leitor = csv.reader(arquivo)
            for linha in leitor :
                 nome,idade ,nota = linha
                 if float (nota) > 8 :
                    print(f"{nome.strip():^15} | {idade.strip():^10} | {nota.strip():^10}")
    elif opcao == "0" :
        print ("Saindo...")
        break
    else :
        print("Opção inválida.")
  
    input("Aperte ENTER para continuar")  
    limpar_tela()