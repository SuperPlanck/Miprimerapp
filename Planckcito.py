import streamlit as st
import pandas as pd
st.title("miprimerapp")
click=st.button("dale click")
st.write("el valor de click es:", click)

if click==True:
    st.image("R.jpg")
    
num1 = st.slider('Elige el numero 1', 0.0,100.0,25.0)
num2 = st.slider('Elige el numero 2',0.0,100.0,25.0)
suma = num1+num2
st.write("la suma de los dos es:", suma)

#Las st.button pusieron botones
#st.button("dale click")
#st.button("Otro boton")

#Este agrego un mapa de la biblioteca de panda
#df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
#st.write(df)
#st.map(df)

#para escribir
#st.write("Hola Mundo")
#st.text("La siguiente es una integral")

#Para insertar formulas
#st.latex("\int_1^6 sin(x)dx")

#para poner titulos bonitos
#st.markdown(" #titulo ")
#st.markdown("*esta es una viñeta*")
