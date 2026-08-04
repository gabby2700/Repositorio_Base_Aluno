import  requests
import streamlit as st
import pandas as pd

cep = st.sidebar.text_input("Digite o CEp que deseja pesquisar",icon="🌍")

if st.sidebar.button("Pesquisar") :
    if len(cep) !=8:
        st.error("CEP inválido,digite sem ponto e traço verifique os digitos")
        st.stop()

    busca = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")

    if busca.status_code == 200:
        dados = busca.json()
        st.write("### Endereço Encontrado:")
        st.write(f"**Rua:** {dados.get('address')}")
        st.write(f"**Bairro:** {dados.get('district')}")
        st.write(f"**Cidade:** {dados.get('city')} - {dados.get('state')}")

        # 3. Exibir no mapa (usando latitude e longitude)
        if "lat" in dados and "lng" in dados:
            lat = float(dados["lat"])
            lon = float(dados["lng"])
            df_mapa = pd.DataFrame({"lat": [lat], "lon": [lon]})
            st.map(df_mapa)
    else:
        st.error("CEP não encontrado no servidor.")
        