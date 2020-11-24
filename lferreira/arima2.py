from Data import  Tcasos as casos
import pandas as pd 
from datetime import datetime as dt 
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX


data = casos()['Magallanes']

#Regulariza fechas
df = pd.DataFrame({'casos':list(data.values)})
df.index=pd.to_datetime(list(data.index))



#Agrupa los datos por meses 

df_month = df.resample('M').mean()

df_month.plot()
#plt.show()


#definir conjunto de datos

x = df_month




#instanciar modelo
sarima_model = SARIMAX(x,order=(2,0,1),seasonal_order=(2, 1, 0, 24))

#ajustar modelo 

results=sarima_model.fit()

# mirar el AIC
#results.aic



#Tomar datos de pruebas , por ejemplo el mes de septiembre , octubre y noviembre

df_09_11 = df_month.loc['2020-09-30':'2020-11-30']
#df_09_11.plot()


# agregar bandas de confianza
pred_1_2_conf = results.get_forecast(steps=24*2).conf_int()
pred_1_2_conf.index = pd.date_range(start='09/30/2020', end='11/30/2020', freq='H')[:-1]
x = pd.date_range(start='11/1/2018', end='11/3/2018', freq='H')[:-1]
y1 = pred_1_2_conf['lower Bici']
y2 = pred_1_2_conf['upper Bici']
plt.fill_between(x, y1, y2, alpha=0.6)

# predecir para Diciembre y enero 2021
pred_1_2 = results.get_forecast(steps=24*2).predicted_mean
pred_1_2.index = pd.date_range(start='12/01/2020', end='12/10/2020', freq='H')[:-1]
pred_1_2.plot()

plt.title('Pronóstico de viajes')
plt.ylabel('Cantidad de viajes')
plt.xlabel('Semana lun-29-oct al vie-02-nov')
plt.legend(('Datos originales octubre', 'Pronóstico noviembre'),
           loc='lower left')
plt.savefig('pronostico.png')
plt.show()