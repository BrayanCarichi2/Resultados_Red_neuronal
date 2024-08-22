import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import altair as alt
import leafmap.colormaps as cm
import fiona
import rasterio
import rasterio.mask

st.set_page_config(layout="wide")





markdown2 = "Esta aplicación muestra de manera muy sencilla, los resultados que son obtenidos mediante el uso de redes neuronales convolucionales. El primer resultado muestra como funciona en la detección y conteo de árboles. El otro resultado, muestra como funciona en la detección de arboles de cítricos."


options = list(
    ['Zonas forestales', 'Arboles de citricos'])
index = options.index('Zonas forestales')




# st.sidebar.title("About")

st.sidebar.info(markdown2)
# st.sidebar.altair_chart(c,use_container_width=True)

enlace1 = ''

st.title("Resultados obtenidos con redes neuronales convolucionales ")

# st.se

i = 1

with st.expander("See source code"):
    selec = st.sidebar.selectbox("Resultados obtenidos", options, index)
    print(selec + "lo seleccionado fue")
    cities = 'geojson/Forestal2.geojson'
    cities2 = 'geojson/citricos.geojson'
    opcion = selec
    if opcion == 'Zonas forestales':
        seleccionado = cities
        

    elif opcion == 'Arboles de citricos':
        seleccionado = cities2
        

    
    
    

    m = leafmap.Map(google_map="HYBRID", center=[25.67, -100.31847], zoom=7, minimap_control=True)
    

    regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'
    regions2 = 'Nl.geojson'

    m.add_geojson(seleccionado, layer_name='Estado de Nuevo León')
    #m2.add_geojson(regions2, layer_name='Estado de Nuevo León')

    # m.add_raster(raster,colormap="terrain",layer_name='DEM')

    
    


m.to_streamlit(height=800)





# streamlit run .\Pages\split_map.py --server.port 8888

#streamlit run Homepage.py --server.port 8888