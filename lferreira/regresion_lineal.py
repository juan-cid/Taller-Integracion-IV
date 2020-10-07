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

n = len(data)+1

x_train = np.arange(1,n,1)
y_train = np.array(y)


algoritmo = linear_model.LinearRegression()
algoritmo.fit(x_train.reshape(-1,1),y_train)


print('w = ' + str(algoritmo.coef_) + ', b = ' + str(algoritmo.intercept_))




# se agregan 100 dias para realizar prediccion
x_nuevo = np.arange(1,n + 100)

# Predecimos los valores y para los datos usados en el entrenamiento
predic = algoritmo.predict(x_nuevo.reshape(-1,1))

#Error Cuadratico medio

# Calculamos el Error Cuadrático Medio (MSE = Mean Squared Error)
#mse = mean_squared_error(y_true = y_train, y_pred = prediccion_entrenamiento)
# La raíz cuadrada del MSE es el RMSE
#rmse = np.sqrt(mse)
#print('Error Cuadrático Medio (MSE) = ' + str(mse))
#print('Raíz del Error Cuadrático Medio (RMSE) = ' + str(rmse))


# calculamos el coeficiente de determinación R2
r2 = algoritmo.score(x_train.reshape(-1,1), y)
print('Coeficiente de Determinación R2 = ' + str(r2))




#Precision del modelo 
print(algoritmo.score(x_train.reshape(-1,1),y_train))



#Graficar los datos
plt.title("Prediccion datos para n + 100 \n ( n =  Dias , cantidad dias datos oficiales 220)")
plt.ylabel("Casos")
plt.xlabel("Dias")


plt.scatter(x_train,y_train,label='Datos Oficiales',color='blue')
plt.plot(predic,color='red',label="Regresion lineal")
plt.legend()
plt.show()
