import pandas as pd

def transformar_datos(df):
    # Lógica de limpieza que ya tenías
    df = df.drop_duplicates()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Close'] > 0] 
    
    # Tus cálculos de Pandas
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['Rendimiento_Diario'] = df['Close'].pct_change() * 100
    
    return df