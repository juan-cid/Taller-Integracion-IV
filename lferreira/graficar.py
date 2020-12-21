import plotly.express as px 
import Data as dget
from pandas import *
from ArimaModel import *

data1 = dget.Tmuertes()
data2 = dget.Tcasos()


columnas = list(data1.columns[1:]) # obtiene las columnas 
regiones = list(data1['Region'])   # obtiene las regiones

#diccionario para guardar los datos
datos = {}

#llena el diccionario con datos vacios
for i in regiones:
	datos[i] = []

#reforma las fechas en formato de pandas
for i in range(len(columnas)):
	columnas[i] = to_datetime(columnas[i],format='%Y%m%d',errors="ignore")


for  i in columnas:
	muertes = data1[i]
	ind = 0 
	for j in datos :
		datos[j].append(muertes[ind])
		ind +=1

#guarda los datos modificados con indice en las fechas
df = DataFrame(datos,index=columnas)




col = ["Los Lagos"]
steps=10
da ={}

for i in range(len(col)) :
	 name = col[i]
	 da[name] = PrediccionCasos(data2[name],steps)
l = []
da2 = {}

#Regulariza los datos de la prediccion para ser guardados en un dataframe
for i in col:
	da2[i] = []
	for j in list(da[i]):
		l.append(j[0])
	da2[i] = l
	l = []


inicio = data2.index[0]
ultimo = data2.index[len(data2)-1]

#obtiene el rango de fecha desde el inicio de la pandemia + los dias de prediccion
range_t = date_range(inicio,periods=len(da2[col[0]]),freq='D')
df = DataFrame(da2,index=range_t)
fig = px.line(df, x=df.index, y=col, title='Cantidad de Muertos')
