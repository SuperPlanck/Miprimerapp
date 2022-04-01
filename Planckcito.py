import streamlit as st
import pandas as pd
st.title("miprimerapp")
#st.button("dale click")
#st.button("Otro boton")
df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
st.write(df)
st.map(df)