import streamlit as st
st.cache
def run_fxn(n: int) -> list:
    return range(n)
def main():
    """Generación de la webapp con streamlit"""
    
    st.title( "MICROBIOLOGIA")
    st.header("LEVADURAS")
    st.subheader("Buttons")
    if st.button("QUE SON"):
        st.text("Streamlit es Cool")
    else:
        st.text("")
    st.subheader("FALSAS LEVADURAS")
    
