import streamlit as st
import pandas as pd
import numpy as np
import Data as dget
from ArimaModel import *
import matplotlib.pyplot as plt

def Prediccion():
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
		steps = 100
		fig = plt.figure()
		plt.title("Prediccion de casos 100 dias ")
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


if opt == "Predicciones Casos":
    Prediccion()
elif opt == "Muertes":
	pass