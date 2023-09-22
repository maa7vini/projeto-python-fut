import streamlit as st
import pandas as pd
import webbrowser

st.write("# FIFA23 OFFICIAL DATASET ⚽")

if "data" not in st.session_state:
    df_data = pd.read_csv("dataset/FIFA23_official_data.csv", index_col=0)
    st.session_state["data"] = df_data

st.sidebar.markdown("Desenvolovido por [maa7vini](https://github.com/maa7vini)")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(
    """
    O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol
    profissionais. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos do jogador,
    características físicas, estatísticas de jogo, detalhes do contrato e afiliações do clube.

    Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para analistas de futebol,
    pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois pois permite estudar 
    atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores
    e desenvolvimento do jogador ao longo do tempo
    
    """
)




