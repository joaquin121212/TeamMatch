import streamlit as st
import webbrowser as wb


st.header("AQUÍ ENCONTRARÁS VIDEOS PARA MEJORAR  ", divider="violet")
def cdo():
    wb.open("https://www.youtube.com/watch?v=zUngFuw2U9g")
st.button("control de oledas", on_click=cdo)
st.header("", divider="violet")
def kiteo():
    wb.open("https://www.youtube.com/watch?v=9YnkxJKek9A")
st.button("kiteo", on_click=kiteo)
st.header("", divider="violet")    
def posicionamiento():
    wb.open("https://www.youtube.com/watch?v=bEjPJpwSy1c")
st.button("posicionamiento", on_click=posicionamiento)
st.header("", divider="violet")
def confg():
    wb.open("https://www.youtube.com/watch?v=br1bZsF7glo")  
st.button("configuracion", on_click=confg)
