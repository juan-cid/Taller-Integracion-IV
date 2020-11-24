from Data import  Tcasos as casos
from pandas.plotting import autocorrelation_plot
from pandas import *
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from datetime import datetime

df = casos()['Magallanes']
df.index =to_datetime(df.index)


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
	#print('Prediccion=%f, experado=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)



start_index= datetime(2020, 12, 1)
end_index = datetime(2020, 12, 30)

prediccion = model_fit.predict(start=start_index, end=end_index)


data =  list(predictions)+list(prediccion)
plt.plot(data,label="Prediccion a 30 dias mas")
plt.legend()
plt.savefig('arima_predict.png')
plt.show()