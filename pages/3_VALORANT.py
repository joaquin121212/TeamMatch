import streamlit as st
import pandas as pd
from io import StringIO

st.header("AQUÍ PODRÁS SUBIR TU CURRÍCULUM DE PRO PLAYER PARA SER CONTACTADO POR UN EQUIPO ", divider="violet")
st.write("déjanos aquí tu currículum para que los equipos puedan explorar tu perfil")



uploaded_file = st.file_uploader("sube tu currículum")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
