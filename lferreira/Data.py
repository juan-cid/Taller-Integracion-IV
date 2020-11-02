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
    return df
def EFallecidos():
	URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto10/FallecidosEtario.csv"
	df  = pd.read_csv(URL)
	return df
