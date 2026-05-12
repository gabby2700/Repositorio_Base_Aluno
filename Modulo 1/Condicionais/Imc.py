
peso= float (input("Digite o seu peso em kg : "))
altura=float(input("Digite a sua altura em m : "))

imc = peso / (altura * altura)

if imc <= 18.5 :
    ("Abaixo do peso")

elif imc <=24.9 :
    print("Peso normal")

elif imc <= 29.9 :
   print ('Sobrepeso')

elif imc >= 34.9 :
   print ("Obesidade Grau 1")

elif imc >= 39.9 :
 print   ("Obesidade grau 2")

else:
  print  ("Obesidade grau 3")





