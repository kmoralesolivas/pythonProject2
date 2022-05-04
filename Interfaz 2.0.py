import streamlit as st
st.cache
def run_fxn(n: int) -> list:
    return range(n)
def main():
    """Generación de la webapp con streamlit"""
    
    st.title( "MICROBIOLOGIA")
    st.header("LEVADURAS")
    st.subheader("Buttons")
    if st.button("Que Son?"):
        st.text("Son hongos microscópicos, habitualmente unicelulares. Aunque la aparición de hongos en nuestros productos alimenticios generalmente nos hace pensar que no es bueno,las levaduras, se llevan usando de forma controlada miles de años
")
    else:
        st.text("")
    st.subheader("FALSAS LEVADURAS")
    
