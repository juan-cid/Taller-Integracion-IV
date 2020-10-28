import streamlit as st
import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto14/FallecidosCumulativo.csv"
df = st.cache(pd.read_csv)(URL)

st.title("Covid19 Fallecidos Cumulativo")

is_check = st.checkbox("Display Data")
if is_check:
    st.write(df)


