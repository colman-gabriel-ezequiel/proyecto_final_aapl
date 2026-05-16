import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.set_page_config(page_title="Market Analytics Dashboard", layout="wide")

st.title("📈 Dashboard de Análisis de Mercado")
st.markdown("Visualización interactiva de los datos procesados en el pipeline ETL")

def levantar_datos():
    conexion = sqlite3.connect('data/finanzas.db')
    df = pd.read_sql("SELECT * FROM activos", conexion)
    conexion.close()
    return df

try:
    df = levantar_datos()
    df['Date'] = pd.to_datetime(df['Date'])

    # Tarjetas con métricas principales (KPIs)
    ultimo_precio = df['Close'].iloc[-1]
    variacion = df['Rendimiento_Diario'].iloc[-1]

    col1, col2 = st.columns(2)
    col1.metric("Último Precio de Cierre", f"${ultimo_precio:,.2f}")
    col2.metric("Variación Diaria", f"{variacion:.2f}%")

    # Gráficos interactivos reaprovechando tu lógica de Matplotlib
    st.subheader("Evolución del Precio, Tendencia (MA50) y Volatilidad")
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, 
                                   gridspec_kw={'height_ratios': [3, 1]})

    ax1.plot(df['Date'], df['Close'], label='Precio de Cierre', color='#1f77b4')
    ax1.plot(df['Date'], df['MA50'], label='Media Móvil 50 días (MA50)', color='#ff7f0e', linewidth=2)
    ax1.set_ylabel('Precio (USD)')
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)

    ax2.bar(df['Date'], df['Rendimiento_Diario'], color='purple', alpha=0.6)
    ax2.axhline(0, color='black', linewidth=0.8)
    ax2.set_ylabel('% Cambio')
    ax2.grid(True, alpha=0.3)

    st.pyplot(fig)

except Exception as e:
    st.warning("La base de datos está vacía o no se encuentra. Ejecutá primero 'python main.py' para poblarla.")