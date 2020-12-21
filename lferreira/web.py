import streamlit as st
import pandas as pd
import numpy as np
import Data as dget
from ArimaModel import *
import plotly.graph_objects as go
import datetime as dt

def Prediccion(steps):
	st.title("Predicciones Casos")

	data = dget.Tcasos()
	options = list(data.columns)
	region_sel = st.sidebar.multiselect(
		"Elegir regiones", options, ["Araucanía","Atacama"]
	)

	#Si la seleccion es 0 
	if len(region_sel) == 0:
		st.error("Por favor, ingrese una región")
	else:
		da ={}
		for i in range(len(region_sel)) :
			 name = region_sel[i]
			 da[name] = PrediccionCasos(data[name],steps)
		l = []
		da2 = {}
		#Regulariza los datos de la prediccion para ser guardados en un dataframe
		for i in region_sel:
			da2[i] = []
			for j in list(da[i]):
				l.append(j[0])
			da2[i] = l
			l = []
		#obtiene el inicio de la fecha de la pandemia
		inicio = data.index[0]
		#obtiene el rango de fecha desde el inicio de la pandemia + los dias de prediccion
		range_t = pd.date_range(inicio,periods=len(da2[region_sel[0]]),freq='D')
		df = pd.DataFrame(da2,index=range_t)
		fig = go.Figure()
		for i in region_sel:
			fig.add_trace(go.Scatter(x=df.index, y=df[i],mode='lines',name="Prediccion "+i))
			fig.add_trace(go.Scatter(x=data.index, y=data[i],mode='lines',
				name="Datos oficiales "+ i))
		st.plotly_chart(fig)

def Muertes(steps):
	st.title("Predicciones Muertes")

	data = dget.Tmuertes()
	options = list(data.columns) 
	region_sel = st.sidebar.multiselect(
			"Elegir regiones", options, ["Araucanía","Atacama"]
	)
	#Si la seleccion es 0 
	if len(region_sel) == 0:
		st.error("Por favor, ingrese una región")
	else:
		da ={}
		for i in range(len(region_sel)) :
			 name = region_sel[i]
			 da[name] = PrediccionMuertes(data[name],steps)
		l = []
		da2 = {}
		#Regulariza los datos de la prediccion para ser guardados en un dataframe
		for i in region_sel:
			da2[i] = []
			for j in list(da[i]):
				l.append(j[0])
			da2[i] = l
			l = []
		#obtiene el inicio de la fecha de la pandemia
		inicio = data.index[0]
		#obtiene el rango de fecha desde el inicio de la pandemia + los dias de prediccion
		range_t = pd.date_range(inicio,periods=len(da2[region_sel[0]]),freq='D')
		df = pd.DataFrame(da2,index=range_t)
		fig = go.Figure()
		for i in region_sel:
			fig.add_trace(go.Scatter(x=df.index, y=df[i],mode='lines',name="Prediccion "+i))
			fig.add_trace(go.Scatter(x=data.index, y=data[i],mode='lines',
				name="Datos oficiales "+ i))
		st.plotly_chart(fig)
# Sidebar   
st.sidebar.title('Navegación')
opt = st.sidebar.radio("",
    ("Predicciones Casos", "Prediccion Muertes")
)

#obtiene el dia actual

today = dt.date.today()
pred = today + dt.timedelta(days=100)


st.sidebar.title("Predicion de datos")
comienzo = st.sidebar.date_input('Comienzo',today)
fin      = st.sidebar.date_input('Fin',pred)
 
steps = (fin-comienzo).days
print(steps)


if(today < pred):
	 st.sidebar.success('Comienzo: `%s`\n\nFecha final:`%s`' % (today, fin))
	 
	 st.sidebar.success("Dias a predecir : "+str(steps) )
	
else:
	st.sidebar.error("Fecha final debe ser mayor a la actual ")

if opt == "Predicciones Casos":
	Prediccion(steps)
elif opt == "Prediccion Muertes":
	Muertes(steps)