from Data import  Tcasos as casos
import matplotlib.pyplot as plt 
from ArimaModel import * 
import pandas as pd
import plotly.express as px



data = casos()['Atacama']
data2= casos()['Maule']





p1 = [PrediccionCasos(data,100),PrediccionCasos(data2,100)]


fig = px.line(p1[0])

fig.show()


