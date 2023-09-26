import streamlit as st
from PIL import Image

st.header("BIENVENIDO A :violet[TeamMatch] ", divider="violet")

st.write("ENCUENTRA TU PRÓXIMO EQUIPO Y TRIUNFA")


image= Image.open("faker.jpg")
st.image (image, caption="")
