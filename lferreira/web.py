import streamlit as st
import pandas as pd
import numpy as np
import Data as dget
from ArimaModel import *
import plotly.express as px 
import datetime as dt

def Prediccion(steps):
	st.title("Predicciones Casos")

	data = dget.Tcasos()
	options = list(data.columns) + ["Todas las regiones"]
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
		fig = px.line(df, x=df.index, y=region_sel)
		st.plotly_chart(fig)

def Muertes(steps):
	st.title("Prediccion Muertes")

	data = dget.Tmuertes()

	print (data)
	# options = list(data.columns) + ["Todas las Regiones"]
	# region_sel = st.sidebar.multiselect("Elegir regiones", options, ["Araucanía","Atacama"])
	# #Si la seleccion es 0 
	# if len(region_sel) == 0:
	# 	st.error("Por favor, ingrese una región")
	# else:
	# 	pass
	# 	print (data)
# Sidebar   
st.sidebar.title('Navegación')
opt = st.sidebar.radio("",
    ("Predicciones Casos", "Muertes")
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
elif opt == "Muertes":
	Muertes(steps)