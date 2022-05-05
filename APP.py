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
    st.sidebar.header("Acerca")
    st.sidebar.text("Genralidades de las levaduras ")

    st.title("MICROBIOLOGIA")
    st.header("LEVADURAS")
    
    today = st.date_input("Hoy es", datetime.datetime.now())
    st.text(f"{today}")
    
    st.subheader("TEMAS")
    if st.button("LEVADURAS"):
        st.text("Las levaduras son hongos microscópicos, habitualmente unicelulares. Aunque la")
        st.text("aparición en nuestros alimentos generalmente nos hace pensar que no es bueno,")
        st. text("cuando se usan de forma controloda pueden llegar a ser beneficiosas.")
        st. text("La levadura  resulta tan importante y útil para nosotros por su capacidad de
        st. text("llevar a cabo la descomposición de azúcares e hidratos de carbono en un proceso 
        st. text("conocido como  fermentación.")

    else:
        st.text("")
  
    if st.button("FALSAS LEVADURAS"):
        st.text("Son hongos microscópicos, habitualmente unicelulares")
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
