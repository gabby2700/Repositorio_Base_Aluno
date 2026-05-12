import streamlit as st 
import calculadora as calc

st.image("https://tse2.mm.bing.net/th/id/OIP.M9uVPDjAkwNUmZOAdu_hKwHaE7?rs=1&pid=ImgDetMain&o=7&rm=3")
st.title("Calculadora('◡')") 

numero1 = st.number_input("Digite o primeiro numero : ", step=0.1,value=None)
numero2 = st.number_input("Digite o segundo numero : ", step=0.1,value=None)
operacao = st.selectbox("Selecione a operação",["+","-","*","/"])
 
if st.button("Calcular") :
    resultado = calc.calcular(numero1, numero2, operacao)
    st.info(f"O resultado é : {resultado}")