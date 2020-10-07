import Data as dget 
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import date


def norma_fecha(fecha):
	f = fecha.split("-")
	return date(int(f[0]),int(f[1]),int(f[2]))
def my_altair_plot(df, value_name, title, option="Normal"):
	df = df.reset_index()
	df = pd.melt(df, id_vars=["fecha"], var_name="Región" , value_name=value_name)
	chart = (
	    alt.Chart(df).mark_line().encode(
	        x="fecha:T",
	        y=alt.Y(value_name, stack=None),
			tooltip = [value_name],
	        color="Región:N",
	    ).properties(
	    	title=title,
			height=600,
	    	width=600
		)
	)
	return chart

def casos():
	data = dget.get_CasosTotales()
	st.title("Casos por regiones")
	options = list(data.columns) + ["Todas las regiones"]
	region_sel = st.sidebar.multiselect(
		"Elegir regiones", options, ["Araucanía","Atacama"]
	)

	if len(region_sel) == 0:
		st.error("Por favor, ingrese una región")


	plot = st.selectbox("Grafico",["Grafico1"])


	#Selecciona el tipo de grafico segun lo seleccionado

	if plot == "Grafico1":
		st.title("------------------------------")
		st.title("Casos Totales region x")

		value_name="Confirmados"

		#Filtra datos de los puestos en 'elegir regiones'

		df = data
		df = df.reset_index()
		df = pd.melt(df, id_vars=["fecha"], var_name="region" , value_name=value_name)


		df_final = pd.DataFrame({'fecha': [], 'region': [],value_name:[]})
		#df_final = pd.melt(df, id_vars=["fecha"], var_name="region" , value_name=value_name)
		for i in range(len(df)):
			for y in region_sel : 
				if df['region'][i] == y:
					#print (df[value_name][i])
					df_final = df_final.append({"fecha":df['fecha'][i],"region":df['region'][i],"Confirmados": df["Confirmados"][i]},ignore_index=True)

		st.dataframe(data)


		chart = (
		    alt.Chart(df_final).mark_line().encode(
		        x="fecha:T",
		        y=alt.Y(value_name, stack=None),
				tooltip = [value_name],
		        color="region:N",
		    ).properties(
		    	title="Total Confirmados",
				height=600,
		    	width=600
			)
		)		
		st.altair_chart(chart)





def muertes():
	data = dget.get_MuertosTotales()

	st.title("Muertes por regiones")
	options = list(data.Region) + ["Todas las regiones"]
	region_sel = st.sidebar.multiselect(
		"Elegir regiones", options, ["Araucanía","Atacama"]
	)

	if len(region_sel) == 0:
		st.error("Por favor, ingrese una región")

<<<<<<< HEAD
	#plot = st.selectbox("Grafico",["Grafico1"])
	

	st.dataframe(data)

	#Selecciona el tipo de grafico segun lo seleccionado

=======
	plot = st.selectbox("Grafico",["Grafico1"])
	



	#Selecciona el tipo de grafico segun lo seleccionado

	if plot == "Grafico1":
		st.title("------------------------------")
		st.title("Muertes Totales region x")

		value_name="Muertes"

		#Filtra datos de los puestos en 'elegir regiones'

		df = data
		fechas = list(data.columns)[1:]
		
	

		start_date = st.sidebar.date_input('Fecha de inicio',norma_fecha(fechas[0]))
		end_date = st.sidebar.date_input('Fecha de término', norma_fecha(fechas[-1]))
		if start_date > end_date:
			st.sidebar.error('Error: La fecha de término debe ser después de la fecha de inicio.')

>>>>>>> prueba









		#df = df.reset_index()
		#df = pd.melt(df, id_vars=["fecha"], var_name="region" , value_name=value_name)



		# df_final = pd.DataFrame({'fecha': [], 'region': [],value_name:[]})
		# #df_final = pd.melt(df, id_vars=["fecha"], var_name="region" , value_name=value_name)
		# for i in range(len(df)):
		# 	for y in region_sel : 
		# 		if df['region'][i] == y:
		# 			#print (df[value_name][i])
		# 			df_final = df_final.append({"fecha":df['fecha'][i],"region":df['region'][i],"Confirmados": df["Confirmados"][i]},ignore_index=True)

		# st.dataframe(df_final)


		# chart = (
		#     alt.Chart(df_final).mark_line().encode(
		#         x="fecha:T",
		#         y=alt.Y(value_name, stack=None),
		# 		tooltip = [value_name],
		#         color="region:N",
		#     ).properties(
		#     	title="Total Confirmados",
		# 		height=600,
		#     	width=600
		# 	)
		# )		
		# st.altair_chart(chart)
# Config
st.beta_set_page_config(
    page_title="Web_1",
 	layout="centered",
 	initial_sidebar_state="expanded",
)

# Sidebar   
st.sidebar.title('Navegación')
opt = st.sidebar.radio("",
    ("Casos", "Muertes")
)


if opt == "Casos":
    casos()
elif opt == "Muertes":
	muertes()