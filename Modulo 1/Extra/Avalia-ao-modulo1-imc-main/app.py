import streamlit as st

st.title("Calculadora IMC 📱")
st.subheader("Feito com Streamilit ❤️")

altura = st.number_input("Digite a sua altura",min_value= 0.0)
peso = st. number_input("Digite o seu peso " , min_value= 0.0)

if st.button("calcular") :
    imc = peso /altura ** 2
    
    if imc < 18.5 :
        st.image("https://www.shutterstock.com/shutterstock/photos/1392715748/display_1500/stock-vector-illustration-of-anorexia-nervosa-man-1392715748.jpg",width = 155)
        st.error("Abaixo do peso")
    elif  imc < 24.9 : 
        st.image("https://image.shutterstock.com/z/stock-vector-beautiful-woman-cartoon-1044974575.jpg" , width = 155)
        st.success("Peso normal")
    elif imc < 29.9 :
        st.image("https://img.freepik.com/premium-vector/man-underwear-with-pear-body-shape-guy-demonstrates-figure-with-wide-hips-happy-male-portrait-trunks-underclothes-flat-vector-illustration-isolated-white-background_198278-26244.jpg?w=2000",width=155)
        st.warning("Sobrepeso")
    elif imc < 34.9 :
        st.image("https://thumbs.dreamstime.com/z/presentaci%C3%B3n-bastante-gorda-de-la-mujer-aislada-en-blanco-personaje-dibujos-animados-muchacha-morena-cauc%C3%A1sica-con-el-pelo-106994404.jpg?w=768",width= 155)
        st.error("Obesidade Grau 1")
    elif imc < 39.9 :
        st.image("https://img.freepik.com/premium-vector/obesity-overweight-people-character-vector-illustration_492281-3561.jpg?w=2000",width= 155)
        st.error("Obesidade Grau 2 ")
    else :
        imc =+ 40.0
        st.image("https://media.istockphoto.com/id/2149952734/es/vector/personaje-de-hombre-completo-con-cuerpo-regordete-de-pie-e-ilustraci%C3%B3n-vectorial-sonriente.jpg?s=1024x1024&w=is&k=20&c=1wBxNsWinkgAXQSmI875vqgafWw41lQr14IjGYdBVmU=",width= 155)
        st.error("Obesidade Grau 3")

            