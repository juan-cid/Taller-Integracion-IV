import pandas as pd


def get_CasosTotales():
    URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo_T.csv"
    df = pd.read_csv(URL)
    df = df.rename(columns={'Region':'Fecha'})
    df.set_index('Fecha',inplace=True)
    df = df.rename_axis(None)
    return df
def get_MuertosTotales():
    URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto14/FallecidosCumulativo.csv"
    df  = pd.read_csv(URL)
    return df
def FallecidosEdad():
	URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto10/FallecidosEtario.csv"
	df  = pd.read_csv(URL)
	return df
