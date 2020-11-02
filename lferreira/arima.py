from Data import  Tcasos as casos
from pandas.plotting import autocorrelation_plot
from pandas import *
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

df = casos()['Magallanes']
df.index =to_datetime(df.index)

#Ajustar modelo

#model = ARIMA(df,order=(2,1,0))
#model_fit= model.fit(disp=0)


#Graficas 

# plot residual errors
#residuals = DataFrame(model_fit.resid)
#residuals.plot()
#plt.show()
#residuals.plot(kind='kde')
#plt.show()
#print(residuals.describe())
#autocorrelation_plot(df)
#plt.show()


#Realizar prediccion

x = df.values
size = int(len(x)*0.7)

# 70% datos de entrenamiento y 30% datos entrenamiento 
train,test =x[0:size],x[size:len(x)]

history = [x for x in train]
predictions = list()

for t in range(len(test)):
	model = ARIMA(history,order=(2,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat=output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('Prediccion=%f, experado=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
plt.plot(test , label="Datos de prueba ")
plt.plot(predictions, color='red' , label="Prediccion")
plt.legend()
plt.savefig('arima_modelo.png')
plt.show()