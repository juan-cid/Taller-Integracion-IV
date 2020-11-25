import streamlit as st
import pandas as pd
import numpy as np
import Data as dget
from ArimaModel import *
import matplotlib.pyplot as plt
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
		fig = plt.figure()
		plt.title("Prediccion de casos "+str(steps)+" dias ")
		for i in range(len(region_sel)) :
			 name = region_sel[i]
			 plt.plot(PrediccionCasos(data[name],steps),label=name)
		plt.legend()
		st.write(fig)





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
	pass