import numpy as np
from Data import get_CasosTotales
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error




data = get_CasosTotales()['Magallanes']

y = []
for i in range(len(data)):
	y.append(data[i])


# x = dias
# y = contagios

x_train = np.arange(1,len(data)+1,1)
y_train = np.array(y)

x_nuevo = np.array([10000])




algoritmo = linear_model.LinearRegression()
algoritmo.fit(x_train.reshape(-1,1),y_train)


print('w = ' + str(algoritmo.coef_) + ', b = ' + str(algoritmo.intercept_))

#Se genera la prediccion

prediccion = algoritmo.predict(x_nuevo.reshape(-1,1))
print(prediccion)



#Error Cuadratico medio

# Predecimos los valores y para los datos usados en el entrenamiento
prediccion_entrenamiento = algoritmo.predict(x_train.reshape(-1,1))

# Calculamos el Error Cuadrático Medio (MSE = Mean Squared Error)
mse = mean_squared_error(y_true = y_train, y_pred = prediccion_entrenamiento)
# La raíz cuadrada del MSE es el RMSE
rmse = np.sqrt(mse)
print('Error Cuadrático Medio (MSE) = ' + str(mse))
print('Raíz del Error Cuadrático Medio (RMSE) = ' + str(rmse))


# calculamos el coeficiente de determinación R2
r2 = algoritmo.score(x_train.reshape(-1,1), y)
print('Coeficiente de Determinación R2 = ' + str(r2))






#Graficar los datos

plt.scatter(x_train,y_train,label='Data',color='blue')
plt.plot(x_train,prediccion_entrenamiento,color='red',label="Regresion lineal")
plt.show()
