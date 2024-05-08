import pandas as pd
import plotly.express as px
import streamlit as st

build_histogram = st.checkbox('Construir un histograma')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_scatter = st.checkbox('Construir un gráfico de dispersión')



if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    fig = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

