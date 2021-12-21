import streamlit as st
import pandas as pd
import sys
import codecs
import streamlit.components.v1 as components
sys.path.append('../')
from PIL import Image
import base64

    

def app():
    data = pd.read_csv("data/movimientos_video.csv")



    st.write("""
        ## ¿Qué movimiento quieres conocer? &#128170;
        #""")

    """### gif from local file"""
    file_ = open("imagenes/crossfit_mov.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(f"<img src='data:image/gif;base64,{data_url}' alt='cat gif' width='600'>",
        unsafe_allow_html=True,)
    # st.image(
    #             "https://wodprep.com/wp-content/uploads/2019/09/Webp.net-gifmaker-2.gif", 
    #             width=500,
    #         ),
    st.sidebar.image("imagenes/Imagen2.png", use_column_width=True)

    size = list(data.name.unique())
    size.insert(0,"Elige")
    input_size = st.selectbox("Elige", size)

    st.write("""
        ### APRENDE SIN LESIONARTE!!
        #""")

    if input_size == "Elige":
        st.stop()
    df = data[data["name"]==input_size]

    movimiento = df["iframe"].values[0]
    components.html(movimiento, height=800),

  
  