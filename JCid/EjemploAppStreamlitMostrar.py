import streamlit as st
import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto14/FallecidosCumulativo.csv"
df = st.cache(pd.read_csv)(URL)

st.title("Covid19 Fallecidos Cumulativo")

is_check = st.checkbox("Display Data")
if is_check:
    st.write(df)


#print(df[216])    
teams = st.sidebar.multiselect("Selecciona Regiones", df['Region'].unique())
#st.write("Tu entrada de dato", teams)

variables = st.sidebar.multiselect("Muestra Regiones y Fechas", df.columns)
#st.write("You selected these variables", variables)

selected_Region_data = df[(df['Region'].isin(teams))]
two_Region_data = selected_Region_data[variables]
Region_data_is_check = st.checkbox("Mostrar los datos de los Regiones y Fechas seleccionados")
if Region_data_is_check:
    st.write(two_Region_data)

st.write(two_Region_data.values)
