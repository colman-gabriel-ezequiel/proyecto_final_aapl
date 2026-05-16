import yfinance as yf
import pandas as pd

def extraer_datos(ticker, inicio='2024-01-01'):
    print(f"Descargando datos para {ticker}...")
    datos = yf.download(ticker, start=inicio)
    
    # Tu truco para aplanar el MultiIndex
    if isinstance(datos.columns, pd.MultiIndex):
        datos.columns = datos.columns.get_level_values(0)
    
    return datos.reset_index()