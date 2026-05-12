programa {
  funcao inicio() {
 
   real valor_desconto,valor_original,valor_final,porcentagem_desconto

   escreva("Digite o valor do produto:")
   leia(valor_original)

   escreva("Digite a porcentagem de desconto:")
   leia(porcentagem_desconto)
   


   valor_desconto= valor_original * (porcentagem_desconto / 100) 

   valor_final= valor_original - valor_desconto
  

   escreva("R$ ",valor_original," com ",porcentagem_desconto,"% de desconto custa: R$ ",valor_final)

  






  }
}
