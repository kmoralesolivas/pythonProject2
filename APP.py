import datetime
import time
import pandas as pd
import streamlit as st
from PIL import Image

@st.cache
def run_fxn(n: int) -> list:
    return range(n)
def main():
    """Generación de la webapp con streamlit"""
    
    st.title("MICROBIOLOGIA")
    st.header("LEVADURAS")
    
    today = st.date_input("Hoy es", datetime.datetime.now())
    st.text(f"{today}")
    st.subheader("Entrada de tiempo")
    
    st.subheader("TEMAS")
    if st.button("LEVADURAS"):
        st.text("Hongos unicelulares")
    else:
        st.text("")
    
    st.subheader("ENCUESTA")
    status = st.radio("APRENDI", ("SI", "NO"))
    if status == "SI":
        st.success("EXCELENTE")
    else:
        st.warning("BYE")
    
    st.subheader("SATISFACCION")
    level = st.slider("QUE TE PARECIO EL CONTENIDO?", 1, 5)
    st.write("Nivel:", level)
    
    st.subheader("Deja aqui un comentario")
    message = st.text_area("Escriba un mensaje")
    if st.button("Aceptar "):
        result = message.title()
        st.success(result)
        
    st.header("Trabajar con archivos de imágenes, audio o vídeos")
    st.subheader("Archivo de imagen")
    img = Image.open("example.jpg")
    st.image(img, width=300, caption="Simple Imagen")
    
    st.subheader("Texto con write")
    st.write("Texto con write")
    st.write(range(10))
    st.header("Desplegando código puro y json")
    st.subheader("Código puro")
    st.code("import numpy as np")
    with st.echo():
        df = pd.DataFrame()
    st.subheader("Desplegando json")
    st.text("Mostrando JSON")
    st.json({"nombre": "Jhon", "apellido": "Doe", "genero": "masculino"})
    st.header("Mostrar barra de progreso, spinner y balloons")
    st.subheader("Barra de progreso")
    my_bar = st.progress(0)
    for p in range(10):
        my_bar.progress(p + 1)
    st.subheader("Spinner")
    with st.spinner("Espere .."):
        time.sleep(5)
        st.success("Finalizó!")
    st.subheader("Balloons")
    
    st.balloons()
    st.header("Trabajando con data science")
    df = pd.read_csv("Venezuela.csv", index_col=0)
    st.subheader("Dataframe")
    st.dataframe(df)
    st.subheader("tabla")
    st.table(df.head())
    st.subheader("gráfica")
    st.line_chart((df))
   
    st.header("Trabajando con funciones")
    st.write(list(run_fxn(10)))
if __name__ == "__main__":
    main()
