
import streamlit as st 
from datetime import datetime

st.sidebar.title("Locadora de Veículos")
st.sidebar.image("logo.png")
carro = st.sidebar.selectbox("Selencione o carro que deseja alugar :",
                    ["Gol","Uno","Voyage","Argo","Porsche 911","Fusca","Volkswagen T-Roc","BMW Bayerische Motoren Werke AG", "Civic" ])

valores_diarias = {"Gol":250, "Uno": 150, "Voyage":350,"Argo":600,"Porsche 911":1700,"Fusca":500,"Volkswagen T-Roc":600,"BMW Bayerische Motoren Werke AG":1200,"Civic":500 }

st.image(f"{carro}.png")
st.subheader(f"Valor da diária: R$ {valores_diarias[carro] }")

data_retirada = st.date_input("Selencione a data de retirada :" ,datetime.now())
data_devolucao = st.date_input("Selecione a data de devuloção :",data_retirada)

if st.button("Alugar"):
    dias = (data_devolucao - data_retirada).days
    total = dias * valores_diarias[carro]
    st.success(f"Alugando o carro por {dias} dias o custo total é: R$ {total}")