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
    st.sidebar.text("Genralidades de las levaduras")
    st.sidebar.text("Tipos de Levaduras")
    st.sidebar.text("Clasificacion")
    st.sidebar.text("Reproduccion")
    st.sidebar.text("Ejemplos")

    st.title("MICROBIOLOGIA")
    st.header("LEVADURAS")
    
    today = st.date_input("Hoy es", datetime.datetime.now())
    st.text(f"{today}")
    
    st.subheader("TEMAS")
    if st.button("LEVADURAS"):
        st.text("Las levaduras son hongos microscópicos, habitualmente unicelulares. Aunque la")
        st.text("aparición en nuestros alimentos generalmente nos hace pensar que no es bueno,")
        st.text("cuando se usan de forma controloda pueden llegar a ser beneficiosas.")
        st.text("Las levaduras que contaminan los alimentos, con frecuencia son especies bien")
        st.text("conocidas que provocan cambios indeseables en ellos. Estos cambios pueden")
        st.text("manifestarse de dos formas, con una turbidez o una formación de una película")
        st.text("en la superficie de los líquidos.")
    else:
        st.text("")
        
    if st.button("TIPOS"):
        st.text("Las levaduras resultan ser muy importantes y útiles para nosotros por su capacidad")
        st.text("de llevar a cabo la descomposición de azúcares e hidratos de carbono en un proceso")
        st.text("conocido como  fermentación. A este tipo se les conoce como fermentativas. Su")
        st.text("metabolismo es facultativo;pueden usar la vía aeróbica o anaeróbica. Las que")
        st.text("oxidan los ácidos orgánicos y el alcohol, y ademas contribuyen en la producción de")
        st.text("los sabores de los vinos, se les conoce como oxidativas. Estas pueden crecer en")
        st.text("forma de película, de velo, o de espuma, y su metabolismom es aerobio.") 
    else:
        st.text("")
  
    if st.button("CLASIFICACION"):
        st.text("Las levaduras que pueden reproducirse sexualmente se conocen como verdaderas,")
        st.text("este proceso implica la formación de ascosporas, sirviendo la propia levadura como") 
        st.text("asca, de aquí que ellas se clasifican como Ascomicetos; por el contrario las falsas")
        st.text("que no producen ascosporas, pertenecen a las levaduras imperfectos.")
    else:
        st.text("")
        
    if st.button("REPRODUCCION"):
        st.text("Puede ser asexualmente, ya sea por fisión binaria en donde una célula se divide")
        st.text("en dos o por gemacion, la cual consiste en la formación de protuberancias llamadas")
        st.text("yemas en la celula madre y que al crecer y desarrollarse,originan nuevos organismos.")
        st.text("Éstos pueden separarse de la celula madre,o bien quedar unidos,formando una colonia.")
        st.text("Existe tambien la reproduccion sexual en donde se liberan las ascosporas que quedan")
        st.text("en el interior de la levadura, y germinan.")
    else:
        st.text("")
        
    if st.button("EJEMPLOS DE LEVADURAS"):
        st.text("1. Genero Schizosaccharomyces:Deterioro de frutas tropicales, melazas y miel.Se")
        st.text("emplea en la desacidificación de vinos, pues metaboliza el ácido málico en alcohol.")
        
        st.text("2. Género Saccharomyces:las especies de este género presentan generalmente células")
        st.text("redondas, ovales o alargadas; algunas pueden formar pseudomicelio. Se reproducen")
        st.text("mayoritariamente por gemación multipolar, aunque también pueden hacerlo por")
        st.text("formación de esporas sexuales. S. cerevisiae es la especie más utilizada. Sus")
        st.text("diferentes variedades llevan a cabo la fermentación del pan, de la cerveza y de los") 
        st.text("vinos.")
        
        st.text("3. Género Pichia: tiene forma oval y puede formar pseudomicelio; es una levadura")
        st.text("oxidativa que forma velos sobre la superficie de vinos y cervezas, alterándolos.")
    
    else:
        st.text("")
        
     if st.button("EJEMPLOS DE FALSAS LEVADURAS"):
         st.text("1. Género Candida: es una levadura que puede formar pseudomicelio, realiza un")
         st.text("metabolismo oxidativo y crece formando velos sobre alimentos salados y de elevada") 
         st.text("acidez, deteriorándolos.")
        
         st.text("2. Género Torulopsis: levaduras fermentativas, redondas u ovaladas, que se reproducen")
         st.text("por gemación multilateral y son causa de muchos problemas en las cervecerías. Algunas")
         st.text("especies pueden alterar la leche condensada, concentrados de frutas y alimentos de")
         st.text("elevada acidez")
        
         st.text("3. Género Kloeckera: son levaduras apiculadas que crecen frecuentemente sobre frutas,")
        st.text("zumos de fruta y vinos, deteriorándolos.")
    
    else:
        st.text("")
    
    st.subheader("ENCUESTA")
    status = st.radio("APRENDI", ("SI", "NO"))
    if status == "SI":
        st.success("EXCELENTE")
    else:
        st.warning("BYE")
    
    st.subheader("SATISFACCION")
    level = st.slider("QUE TE PARECIO EL CONTENIDO?", 1, 10)
    st.write("Nivel:", level)
    
    st.subheader("Deja aqui un comentario")
    message = st.text_area("Escriba un mensaje")
    if st.button("Aceptar "):
        result = message.title()
        st.success(result)
        
if __name__ == "__main__":
     main()
