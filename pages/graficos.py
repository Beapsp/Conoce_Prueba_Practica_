import streamlit as st
import pandas as pd
from PIL import Image
#import src.manage_data as dat
#import plotly.express as px
import codecs
import streamlit.components.v1 as components
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns

def soniadice(x):
    ay = x.split(" ")
    print(ay)
    if len(ay) > 1:
        return ay[1]
    else:
        return "(17-34)"



def app():
    
    st.write("""
        ## ¿Quieres saber un poco más? 
        #### GAMES --> La competición de Crossfit por excelencia a nivel mundial
        #### OPEN --> competición clasificatoria para los Crossfit Games
        #""")
    
    size2 = ["Competición","Games","Open"]
    input_size = st.selectbox("Elige", size2)
    # grafico1 = pd.read_csv("data/redi_games.csv")
    # grafico2 = pd.read_csv("data/clean_games.csv")
    grafico3 = pd.read_csv("data/unique_several.csv")
    # grafico5 = pd.read_csv("data/top5_w_open.csv")
    # grafico7 = pd.read_csv("data/clean_open19.csv")

        #st.markdown("![Alt Text](https://monophy.com/media/3osBLvoR8tGE6OI5os/monophy.gif)") importar gif sin size
    #st.image(
                #"https://monophy.com/media/3osBLvoR8tGE6OI5os/monophy.gif", 
                #width=700,
            #)
    
    
    if input_size == "Competición":
        st.image(
                "https://monophy.com/media/3osBLvoR8tGE6OI5os/monophy.gif", 
                width=700,
            ),

    
        
    elif input_size == "Games":

        st.write("""
        ## Participación en GAMES por países 
        #""")

        st.write(""" 
        ##### LA MAYOR PARTICIPACIÓN SE DA EN EE.UU, CANADÁ Y AUSTRALIA
        #""")

        mapita = codecs.open("html/mapa.html","r")
        mapita_r=mapita.read()
        components.html(mapita_r, height=900,width=900, scrolling = True)

      

        # fig = go.Figure(go.Choropleth(
        #     locations = grafico1['countryoforiginname'],
        #     locationmode = "country names",
        #     z = grafico1['competitorname'],
        #     text = grafico1['countryoforiginname'],
        #     colorscale = 'magma',
        #     autocolorscale=False,
        #     reversescale=True,
        #     marker_line_color='#efefef',
        #     marker_line_width=0.1,
        #     #colorbar_ticksuffix = '%',
        #     colorbar_title = 'Number competitors',
        #     )
        # )
        
        # # Establecemos las características del título y la apariencia del mapa base
        # fig.update_layout(
        #     title_text = 'LA MAYOR PARTICIPACIÓN SE DA EN EE.UU, CANADÁ, AUSTRALIA',
        #     showlegend = False,
        #     geo = dict(
        #         scope='world',
        #         resolution=50,
        #         projection_type='miller',
        #         showcoastlines=True,
        #         showocean=True,
        #         showcountries=True,
        #         oceancolor='#eaeaea',
        #         lakecolor='#eaeaea',
        #         coastlinecolor='#dadada'
        #     )
        # ).update_layout(width=1000,height=1000)
 
        # st.plotly_chart(fig),



        st.write("""
        ## Media de edad participantes 
        ###### LA MEDIA DE EDAD GENERAL ES DE 33 AÑOS, MIENTRAS QUE LA MEDIANA ES DE 30 AÑOS""")
       
        media_mediana = codecs.open("html/media_mediana.html","r")
        maedia_r=media_mediana.read()
        components.html(maedia_r, height=500,width=900, scrolling = True)

        # fig3 = px.histogram(grafico2, x="age")
        # fig3.add_vline(grafico2.age.median(), line_width=3, line_dash="dash", line_color="purple")
        # fig3.add_vline(grafico2.age.mean(), line_width=3, line_dash="dash", line_color="green")
        # st.plotly_chart(fig3),
        st.write("""
        ## Edad media, mínima y máxima
        ###### LA PERSONA MÁS JOVEN QUE PARTICIPA EN LOS GAMES ES UNA MUJER Y LA PERSONA MÁS MAYOR ES UN HOMBRE""")
       
        media_mediana = codecs.open("html/edadminmax.html","r")
        maedia_r=media_mediana.read()
        components.html(maedia_r, height=500,width=900, scrolling = True)
        
        st.write("""
        ## Participación general Mujeres y Hombres 
        ###### LA DIFERENCIA DE PARTICIPACIÓN GENERAL ENTRE HOMBRES Y MUJERES ES MUY PEQUEÑA""")

        gender = codecs.open("html/gender.html","r")
        gender_r=gender.read()
        components.html(gender_r, height=500,width=900, scrolling = True)

        # fig2 = px.histogram(grafico2, x="gender")
        # fig2.update_layout(bargap=0.2)
        # st.plotly_chart(fig2),


        st.write("""
        ## Participación por rangos de edad 
        ###### PARTICIPACIÓN HOMBRES > MUJER **SOLO** EN RANGO DE EDAD GENERAL""")

        gender_par = codecs.open("html/gender_par.html","r")
        gender_par_r=gender_par.read()
        components.html(gender_par_r, height=500,width=900, scrolling = True)

        # agrupado =pd.DataFrame(grafico2.groupby(["division"])["gender"].value_counts())
        # agrupado.rename(columns={"gender":"count"}, inplace=True)
        # agrupado.reset_index(inplace=True)
        # agrupado["categorias"] = agrupado["division"].apply(soniadice)
        # fig4 = px.histogram(agrupado, x='categorias', y="count", color="gender", barmode='group')
        # fig4.update_layout(bargap=0.2)
        # st.plotly_chart(fig4),


    else:



        # st.write("""
        # ## Participación de mujeres en países vecinos 
        # #""")
        # portada = Image.open("imagenes/image7.jpg")
        # st.image(portada, use_column_width=True)

        # st.write("""
        # ## Edades mínima, media, máxima 
        # #""")
        # fig6 = px.box(grafico2, x="division", y="age", color="gender", color_discrete_map={1: '#19D3F3', 0: 'red'}) 
        # fig6.update_layout(width=900,height=500)
        # st.plotly_chart(fig6),


        st.write("""
        ## Mujeres que representan solas a su país
        #""")
        st.write(""" 
        ##### LA MAYORÍA DE ATLETAS CROSSFITERAS REPRESENTAN DE MANERA ÚNICA A SU PAÍS
        #""")
        
        unique = codecs.open("html/several_unique.html","r")
        unique_r=unique.read()
        components.html(unique_r, height=500,width=900, scrolling = True)

        
        
        # fig5 = px.bar(grafico3, x="competitors", y="countryoforiginname", color = "division")
        # fig5.update_layout(width=900,height=500)
        # st.plotly_chart(fig5),
        
        st.write("""
        ## Top 10 países ranking mundial OPEN
        #""")
        st.write(""" 
        ##### ESPAÑA FIGURA EN EL TOP10 POR RANKING GENERAL A NIVEL MUNDIAL 
        #""")
        portada = Image.open("imagenes/top10.png")
        st.image(portada, use_column_width=True)

        


        st.write("""
        ## España en el top10 
        #""")
        st.write(""" 
        ##### DE LOS TRES ATLETAS QUE HACEN QUE ESPAÑA ENTRE EN EL TOP10 MUNDIA, UNA ES UNA MUJER
        
        #""")
        portada = Image.open("imagenes/top10_ES.png")
        st.image(portada, use_column_width=True)

        

        st.sidebar.image("imagenes/Imagen2.png", use_column_width=True)

        # st.write("""
        # ## Pesos por rangos de edad en mujeres 
        # #""")
        # fig7 = fig = px.scatter(grafico5, x="age", y="weight", color="division_y")
        # fig7.update_layout(width=900,height=500)
        # st.plotly_chart(fig7),

        
        
       