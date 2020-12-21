from Data import  Tcasos as casos
import pandas as pd 
from datetime import *
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
import numpy as np
import plotly.express as px


def PrediccionCasos(data,steps):
	#Regulariza fechas
	df = pd.DataFrame({'casos':list(data.values)})
	df.index=pd.to_datetime(list(data.index))
	# create a differenced series
	def difference(dataset, interval=1):
		diff = list()
		for i in range(interval, len(dataset)):
			value = dataset[i] - dataset[i - interval]
			diff.append(value)
		return np.array(diff)
	# invert differenced value
	def inverse_difference(history, yhat, interval=1):
		return yhat + history[-interval]

	x = df.values
	days_in_month = 30
	differenced = difference(x, days_in_month)
	# fit model
	model = ARIMA(differenced, order=(7,0,1))
	model_fit = model.fit(disp=0)
	# print summary of fit model
	#print(model_fit.summary())

	# one-step out-of sample forecast
	forecast = model_fit.forecast()[0]

	forecast = inverse_difference(x, forecast, days_in_month)
	#print('Forecast: %f' % forecast)
	# multi-step out-of-sample forecast
	forecast = model_fit.forecast(steps=steps)[0]
	# invert the differenced forecast to something usable
	history = [x for x in x]
	day = 1
	for yhat in forecast:
		inverted = inverse_difference(history, yhat, days_in_month)
		#print('Day %d: %f' % (day, inverted))
		history.append(inverted)
		day += 1

	return history

def PrediccionMuertes(data,steps):
		#Regulariza fechas
	df = pd.DataFrame({'muertes':list(data.values)})
	df.index=pd.to_datetime(list(data.index))
	# create a differenced series
	def difference(dataset, interval=1):
		diff = list()
		for i in range(interval, len(dataset)):
			value = dataset[i] - dataset[i - interval]
			diff.append(value)
		return np.array(diff)
	# invert differenced value
	def inverse_difference(history, yhat, interval=1):
		return yhat + history[-interval]

	x = df.values
	days_in_month = 30
	differenced = difference(x, days_in_month)
	# fit model
	model = ARIMA(differenced, order=(7,0,1))
	model_fit = model.fit(disp=0)
	# print summary of fit model
	#print(model_fit.summary())

	# one-step out-of sample forecast
	forecast = model_fit.forecast()[0]

	forecast = inverse_difference(x, forecast, days_in_month)
	#print('Forecast: %f' % forecast)
	# multi-step out-of-sample forecast
	forecast = model_fit.forecast(steps=steps)[0]
	# invert the differenced forecast to something usable
	history = [x for x in x]
	day = 1
	for yhat in forecast:
		inverted = inverse_difference(history, yhat, days_in_month)
		#print('Day %d: %f' % (day, inverted))
		history.append(inverted)
		day += 1

	return history


