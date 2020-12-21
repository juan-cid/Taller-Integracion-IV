import plotly.graph_objects as go
import Data as dget
from pandas import *
from ArimaModel import *

data1 = dget.Tmuertes()
data2 = dget.Tcasos()

col = ["Los Lagos"]
steps=100
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
fig = go.Figure()
#px.line(df, x=df.index, y=col, title='Cantidad de Muertos')
fig.add_trace(go.Scatter(x=df.index, y=df[col[0]],mode='lines',name=col[0]))
fig.add_trace(go.Scatter(x=data2.index, y=data2[col[0]],mode='lines',
	name="Datos oficiales "+ col[0]))
fig.show()