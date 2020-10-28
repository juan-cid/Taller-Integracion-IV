from pandas import DataFrame
from Data import get_CasosTotales
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


data = get_CasosTotales()['Magallanes']

y = []
x = []
for i in range(len(data)):
	y.append(data[i])
	x.append(i+1)

df = DataFrame({'x':x,'y':y})
# x = dias
# y = contagios


#Ubicar centroides de los datos


kmeans = KMeans(n_clusters=5).fit(df)
centroids = kmeans.cluster_centers_

plt.title("Casos totales para Magallanes")
plt.scatter(df['x'],df['y'],c=kmeans.labels_.astype(float),s=50,alpha=0.5)
plt.scatter(centroids[:,0],centroids[:,1],c='red',s=50)
plt.savefig('kmeans.png')
plt.show()