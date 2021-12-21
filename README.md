# Conoce-prueba-practica_

![imagen](imagenes/image.jpg)

## OBJETIVO:
Este proyecto se ha llevado a cabo con dos claros objetivos, por un lado analizar datos para dar a conocer el deporte del crossfit así como para dar visibilidad a las mujeres que lo practican, y por otro motivar y facilitar información al usuario para que lo practique.

## EJECUCIÓN:
Se ha dividido el proyecto en 3 fases diferenciadas:
- ### Fase de limpieza, análisis y visualización de datos:
    Se parte de varios datasets de diferentes competiciones de diferentes años, los cuales se han limpiado y analizado sus datos en base a unas hipótesis que se visualizarán finalmente. Estas hipótesis son:
    - El país donde más atletas participan a nivel mundia es EE.UU.
    - La media de edad de participantes es de 29 años
    - Hay más participantes hombres que mujeres
    - La media de edad de participantes es de 29 años
    - Hay más participantes hombres que mujeres
    - El participante más joven y más mayor es un hombre
    - La mayoría de mujeres paticipan en equipo representando a su país
    - España se encuentra en el top10 del ranking general mundial


- ### Scrapeo web:
Para conseguir los nombres de todos los movimientos que se realizan en esta práctica y que además muestre al usuario un video explicativo de cómo se ejecuta dicho movimiento sin lesiones, se ha realizado un screapeo de la web de [https://www.crossfit.com/]


- ### Llamada a la API de Google:
Para poder recomendar al usuario todos los boxes de Crossfit cercanos a la dirección que este decida, se hace una llamada "en caliente" a la Api de Google, mostrando además, el listado del resultado con la dirección completa, según el rating obtenido en Google


## ¿QUÉ CONCLUSIÓN HE OBTENIDO?
- Las conclusiones medibles se obtienen de la Fase 1:
  - El país donde más atletas participan a nivel mundia es EE.UU --> se cumple mi hipótesis
  - La media de edad de participantes es de 29 años --> se refuta mi hipótesis, la edad media es de 33 años
  - Hay más participantes hombres que mujeres --> se cumple mi hipótesis, aunque analizando la participación por rangos de edad, solo participan más hombres en el rango de (17-34) años
  - El participante más joven y más mayor es un hombre --> se refuta mi hipótesis, la persona más joven que participa en los GAMES es una mujer
  - La mayoría de mujeres paticipan en equipo representando a su país --> se refuta mi hipótesis, la mayoría de mujeres acuden solas a representar su país
  - España se encuentra en el top10 del ranking general mundial --> se cumple mi hipótesis

## ESTRUCTURA DEL PROYECTO:

- Una carpeta "data" con todos los dataset utilizados para la ejecución de la primera fase.
- Una carpeta "html" con todos los gráficos exportados en esta html para visualizarlos en streamlit.
- Una carpeta "imágenes" con todas las imágenes utilizadas a lo largo del proyecto.
- Una carpeta "Notebooks" con los siguientes archivos:
    - Un jupyter notebook de limpieza de datos --> "cleaning_cross.
    - Un jupyter notebook de visualización --> "visualization".
    - Un jupyter notebook con el scrapeo web realizado --> "web_scraping-videos"
    - Un jupyter notebook con la llamada a la Api de Google para extraer las coordenas de la dirección deseada --> "coordenadas geopy"
- Una carpeta "pages" con todos los archivos.py necesarios para visualizar streamlit
- Una carpeta "src" con los archivos que contienen las funciones utilizadas en toda la ejecución del proyecto.
- Un archivo "Streamlit" donde se muestra un video de la presentación llevada a cabo. Se adjuntan imágenes a continuación:

![imagen1](imagenes/streamlit2.jpg)
![imagen2](imagenes/streamlit3.jpg)
![imagen3](imagenes/streamlit4.jpg)





## RECURSOS UTILIZADOS:

        [pandas](https://pandas.pydata.org/)

        [numpy](https://numpy.org/doc/)

        [regex](https://docs.python.org/3/library/re.html)

        [seaborn](https://seaborn.pydata.org/)

        [matplotlib](https://matplotlib.org/)

        [selenium](https://www.selenium.dev/selenium/docs/api/py/api.html)
        
        [beautifulsoup](https://beautiful-soup-4.readthedocs.io/en/latest/)

        [folium](http://python-visualization.github.io/folium/)

        [geopy](https://geopy.readthedocs.io/en/stable/)

        [streamlit](https://docs.streamlit.io/)
        """)

![imagenn](imagenes/streamlit1.jpg)       