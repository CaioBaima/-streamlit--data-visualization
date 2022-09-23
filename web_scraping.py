# Importando bibliotecas necessárias

import requests
import pandas as pd
import os
import streamlit as st

st.markdown('Selecione a rodada que quer analisar')
rodada = st.slider('', 1, 38)

# Criando uma variável para cada link de tabela
# pd.head_html em cada uma das variáveis
if st.button(f'Clique para confirmar que deseja analisar o Brasileirão até a {rodada}º rodada.'):

    for i in range(1, rodada + 1):
        globals()[f'df_{i}'] = pd.read_html(requests.get(f'https://www.worldfootball.net/schedule/bra-serie-a-2022-spieltag/{i}/').text)

    # Já identifiquei testando que a tabela que me interessa está no índice [3]
    # É possível veficar usando o seguinte comando: df_21[3].head()

    # Agoa vou salvar as tabelas.

    os.makedirs('tabelas_brasileirao', exist_ok=True)
    for i in range(1, rodada + 1):
        globals()[f'df_{i}'][3].to_csv(f'tabelas_brasileirao/rodada_{i}.csv')
