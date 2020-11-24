from Data import  Tcasos as casos
import matplotlib.pyplot as plt 
from ArimaModel import * 
import pandas as pd
data = casos()['Atacama']
data2= casos()['Maule']




p1 = [PrediccionCasos(data,100),PrediccionCasos(data2,100)]


plt.plot(p1[0],label='Atacama')
plt.plot(p1[1],label='Maule')
plt.legend()
plt.show()



