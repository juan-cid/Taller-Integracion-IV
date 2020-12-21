import pandas as pd

def Tcasos():
    URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo_T.csv"
    df = pd.read_csv(URL)
    df = df.rename(columns={'Region':'Fecha'})
    df.set_index('Fecha',inplace=True)
    df = df.rename_axis(None)
    return df
def Tmuertes():
    URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto14/FallecidosCumulativo.csv"
    df  = pd.read_csv(URL)
    
    columnas = list(df.columns[1:]) # obtiene las columnas 
    regiones = list(df['Region'])   # obtiene las regiones

    #diccionario para guardar los datos
    datos = {}
    #llena el diccionario con datos vacios
    for i in regiones:
        datos[i] = []
    #reforma las fechas en formato de pandas
    for i in range(len(columnas)):
        columnas[i] = pd.to_datetime(columnas[i],format='%Y%m%d',errors="ignore")
    for  i in columnas:
        muertes = df[i]
        ind = 0 
        for j in datos :
            datos[j].append(muertes[ind])
            ind +=1

    #guarda los datos modificados con indice en las fechas
    df = pd.DataFrame(datos,index=columnas)
    return df



def EFallecidos():
	URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto10/FallecidosEtario.csv"
	df  = pd.read_csv(URL)
	return df
