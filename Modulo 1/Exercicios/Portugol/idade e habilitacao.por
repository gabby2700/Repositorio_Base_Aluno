programa {
  funcao inicio() {
    
    inteiro idade
    cadeia habilitacao
    logico podeDirigir


    escreva("Digite a sua idade: ")
    leia(idade)


    escreva("Digite se possuí habilitação [S para sim | N para não]: ")
    leia(habilitacao)


    podeDirigir = idade >= 18 e habilitacao == "S"


    escreva("Essa pessoa pode dirigir? ", podeDirigir) 














  }
}
