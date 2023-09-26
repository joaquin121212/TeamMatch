import streamlit as st
from PIL import Image


st.header("CONTÁCTANOS ", divider="violet")
st.write("PARA HABLAR CON NOSOTROS SOBRE ALGÚN ERROR DE LA PÁGINA O SUGERENCIA UTILIZA EL SIGUIENTE MAIL")
st.write("TeamMachtCompany@gmail.com")

image = Image.open('logo4.jpg')

st.image(image, caption='')


st.write("CREADORES")
st.write("CEO: Joaquín de la puente")
st.write("Product Manager: Antonia vásquez")
st.write("Developer: Agustín llantén")
st.write("curso: 4to green")
