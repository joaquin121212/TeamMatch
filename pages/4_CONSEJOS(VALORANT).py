import streamlit as st
import webbrowser as wb


st.header("AQUÍ ENCONTRARÁS VIDEOS PARA MEJORAR  ", divider="violet")

def aim():
    wb.open("https://www.youtube.com/watch?v=DeFSBVQmjYg")
st.button("rutina de aim", on_click=aim)
st.header("", divider="violet")   
def pos():
    wb.open("https://www.youtube.com/watch?v=T1nrBfH5ghA")
st.button("posicionamiento", on_click=pos)
st.header("", divider="violet")
def mira():
    wb.open("https://www.youtube.com/watch?v=SfIq646Xy98")
st.button("miras", on_click=mira)        