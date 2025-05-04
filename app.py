import streamlit as st
import pandas as pd 
import plotly.express as px 


#Carga del DataFrame
df_vehicles_us = pd.read_csv('vehicles_us.csv') 

# Encabezado de la app
st.header ('analisis de anuncion de vehículos en USA')

# Boton de casilla para mostrar histograma: 

if st.checkbox('Mostrar histograma del odometro'):
    st.write('histograma de la Odometro')
    fig_hist = px.histogram(df_vehicles_us, x='odometer', nbins=30, title = 'Distribucion de odometro')
    st.plotly_chart(fig_hist)

# Boton de casilla para mostrar grafico de dispersion

if st.checkbox('Grafico de dispersion precio vs año'):
    st.write('Grafico de dispersion entre el precio y el año del vehiculo')
    fig_scatter= px.scatter(df_vehicles_us, x= 'model_year' , y='price', 
                            title= 'Precio vs Año del vehiculo', 
                            labels={'model_year':'Año del modelo','price': 'Precio'},
                            opacity= 0.5)
    st.plotly_chart(fig_scatter)



