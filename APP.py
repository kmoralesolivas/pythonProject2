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
    
    st.write(list(run_fxn(10)))
if __name__ == "__main__":
    main()
