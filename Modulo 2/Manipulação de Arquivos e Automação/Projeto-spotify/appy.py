import streamlit as st

musicas = {
    "Michael Jackson":{
        "Remember the time":"https://www.youtube.com/watch?v=LeiFF0gvqcc&list=RDLeiFF0gvqcc&start_radio=1",
        "They Don't Care Aboout Us":"https://www.youtube.com/watch?v=QNJL6nfu__Q&list=RDLeiFF0gvqcc&index=2",
        "You Rock My World":"https://www.youtube.com/watch?v=1-7ABIM2qjU&list=RD1-7ABIM2qjU&start_radio=1",
        "Chicago":"https://www.youtube.com/watch?v=wAoq__SQpwk&list=RDwAoq__SQpwk&start_radio=1",
        "Black Or white":"https://www.youtube.com/watch?v=F2AitTPI5U0&list=RDF2AitTPI5U0&start_radio=1",
        "Love Never Felt So Good":"https://www.youtube.com/watch?v=TTzD6gWV16s&list=PLs0odKA07LBY8gO6GTwiXcCsqDdpoMIwR"
},

    "Lalisa":{
        "Bad Angel":"https://www.youtube.com/watch?v=dKmPEhJ4wjY&list=RDdKmPEhJ4wjY&start_radio=1",
        "Rockstar":"https://www.youtube.com/watch?v=hbcGx4MGUMg&list=RDhbcGx4MGUMg&start_radio=1",
        "New Woman":"https://www.youtube.com/watch?v=UxXY_hR_wzo&list=RDUxXY_hR_wzo&start_radio=1",
        "Moonlit Floor":"https://www.youtube.com/watch?v=pxGM_TOgHuM&list=RDpxGM_TOgHuM&start_radio=1"
    },

    "Xdinary heroes":{
        "Voyager":"https://www.youtube.com/watch?v=ZeNOs_7kqaw&list=RDZeNOs_7kqaw&start_radio=1",
        "Beautiful Life":"https://www.youtube.com/watch?v=9iV-RmWapk8&list=RD9iV-RmWapk8&start_radio=1",
        "ICU":"https://www.youtube.com/watch?v=L4rOBdjcwLc&list=RDL4rOBdjcwLc&start_radio=1",
        "Night before the end":"https://www.youtube.com/watch?v=B93haFHobpg&list=RDB93haFHobpg&start_radio=1",
        "Fire":"https://www.youtube.com/watch?v=y9siAY03BCQ&list=RDyhttps://www.youtube.com/wat9siAY03BCQ&start_radio=1",
        "iNSTEAD!":"https://www.youtube.com/watch?v=ZCXkOGH6azI&list=RDZCXkOGH6azI&start_radio=1",
        "Save me":"https://www.youtube.com/watch?v=Ooi3uic6lNc&list=RDOoi3uic6lNc&start_radio=1"
    },

    "XG":{
        "HYPNOTIZE":"https://www.youtube.com/watch?v=cUfDOS2SINM&list=RDcUfDOS2SINM&start_radio=1",
        "LEFT RIGHT":"https://www.youtube.com/watch?v=T6YVgEpRU6Q&list=RDEMms31BDMLf9pUh2PWQ2bLBg&index=1",
        "IS THIS LOVE":"https://www.youtube.com/watch?v=aHTI0SXGVS0&list=RDEMms31BDMLf9pUh2PWQ2bLBg&index=3",
        "MILLION PLACES":"https://www.youtube.com/watch?v=c5Fc6r4A9d8&list=RDEMms31BDMLf9pUh2PWQ2bLBg&index=15",
        "SHOOTING STAR":"https://www.youtube.com/watch?v=G8GHuJcNWtI&list=RDG8GHuJcNWtI&start_radio=1"
    }

}


st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("Selecione o artista ", musicas.keys())
musicas_artista = musicas[artista]

st.title(artista)
for musica in musicas_artista.items():
    título,link = musica
    st.subheader(título)
    st.video(link)