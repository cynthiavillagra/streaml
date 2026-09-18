import streamlit as st


st.set_page_config(page_title="Mi app Streamlit", page_icon=":wave:")

st.title("Hola, Streamlit")
st.write("Esta es una aplicación básica creada con Streamlit.")

nombre = st.text_input("¿Cómo te llamas?")

if nombre:
    st.success(f"¡Hola, {nombre}!")