import streamlit as st
from PIL import Image



def app():

    st.write("""
        ## Motivación
        ##### Desmontar mitos relacionados con la idea general que se tiene del Crossfit
        ##### Motivar a todo el mundo a que al menos pruebe a practicarlo
        #""")
    

    st.write("""
        ## ¿Cómo lo he conseguido?
        ##### Dividiendo mi proyecto en 3 fases:
        #""")
    
    st.write("""
        ### Limpieza, análisis y visualización 
        ##### A partir de varios datasets de diferentes competiciones de diferentes años, he limpiado y analizado dichos datos en base a unas hipótesis que visualizar
        - El país donde más atletas participan a nivel mundia es EE.UU
        - La media de edad de participantes es de 29 años
        - Hay más participantes hombres que mujeres
        - El participante más joven y más mayor es un hombre
        - La mayoría de mujeres paticipan en equipo representando a su país
        - España se encuentra en el top10 del ranking general mundial

        #""")

    portada = Image.open("imagenes/met.png")
    st.image(portada, use_column_width=True)

    st.write("""
        ### Scrapeo web
        ##### Para conseguir los nombres de todos los movimientos que se realizan en esta práctica y que además muestre al usuario un video explicativo de cómo se ejecuta dicho movimiento sin lesiones, he scrapeado la web de crossfit.com
    
        #""")

    portada = Image.open("imagenes/scrapeo.jpg")
    st.image(portada, use_column_width=True)




    st.write("""
        ### Llamada API Google
        ##### Para poder recomendar al usuario todos los boxes de Crossfit cercanos a la dirección que decida, hago una llamada "en caliente" a la Api de Google, mostrando además el listado del resultado con la dirección completa, según el rating obtenido en Google
        #""")

    portada = Image.open("imagenes/apigoo.jpg")
    st.image(portada, use_column_width=True)

    st.write("""
        ## ¿Qué conclusiones he obtenido?
        ##### Fase 1:
        - El país donde más atletas participan a nivel mundia es EE.UU --> se cumple mi hipótesis
        - La media de edad de participantes es de 29 años --> se refuta mi hipótesis, la edad media es de 33 años
        - Hay más participantes hombres que mujeres --> se cumple mi hipótesis, aunque analizando la participación por rangos de edad, solo participan más hombres en el rango de (17-34) años
        - El participante más joven y más mayor es un hombre --> se refuta mi hipótesis, la persona más joven que participa en los GAMES es una mujer
        - La mayoría de mujeres paticipan en equipo representando a su país --> se refuta mi hipótesis, la mayoría de mujeres acuden solas a representar su país
        - España se encuentra en el top10 del ranking general mundial --> se cumple mi hipótesis
        #""")

    st.write("""
        ## Librerías utilizadas
        
    
        [pandas](https://pandas.pydata.org/)

        [numpy](https://numpy.org/doc/)

        [regex](https://docs.python.org/3/library/re.html)

        [seaborn](https://seaborn.pydata.org/)

        [matplotlib](https://matplotlib.org/)

        [folium](http://python-visualization.github.io/folium/)

        [geopy](https://geopy.readthedocs.io/en/stable/)

        [streamlit](https://docs.streamlit.io/)
        """)
    st.sidebar.image("imagenes/Imagen2.png", use_column_width=True)