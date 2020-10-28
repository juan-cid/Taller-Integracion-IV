import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from Data import *
import plotly.graph_objects as go
from sklearn import linear_model
from sklearn.metrics import mean_squared_error



data = get_CasosTotales()['Magallanes']

y = []
for i in range(len(data)):
    y.append(data[i])


# x = dias
# y = contagios

n = len(data)+1

x_train = np.arange(1, n, 1)
y_train = np.array(y)


algoritmo = linear_model.LinearRegression()
algoritmo.fit(x_train.reshape(-1, 1), y_train)


print('w = ' + str(algoritmo.coef_) + ', b = ' + str(algoritmo.intercept_))


# se agregan 100 dias para realizar prediccion
x_nuevo = np.arange(1, n + 100)

# Predecimos los valores y para los datos usados en el entrenamiento
predic = algoritmo.predict(x_nuevo.reshape(-1, 1))



#print(x_train)

#print(y_train)



fig = go.Figure()

fig.add_trace(go.Scatter(x=x_train, y=y_train, mode='lines+markers', name='Datos'))
fig.add_trace(go.Scatter(name='Regresion lineal',x=x_train ,y=predic, mode='lines'))

st.plotly_chart(fig, use_container_width=True)
