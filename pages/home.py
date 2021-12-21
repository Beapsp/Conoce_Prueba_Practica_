import streamlit as st
from PIL import Image
import base64
#import streamlit.components.v1 as components
#import codecs
#gif = 'https://i.pinimg.com/originals/74/65/1d/74651dc9fc122bf6847c597d97da7ed0.gif'

def app():

    """### gif from local file"""
    file_ = open("imagenes/crossfit.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f"<img src='data:image/gif;base64,{data_url}' alt='cat gif' width='600'>",
        unsafe_allow_html=True,
    )

    st.sidebar.image("imagenes/Imagen2.png", use_column_width=True)
    #portada = Image.open("imagenes/image5.jpg")
    #st.image(portada, use_column_width=True)
    #f=codecs.open("data/pedrito.html", 'r')
    #pedro = f.read()

    #components.html(pedro,height=550,scrolling=True)


