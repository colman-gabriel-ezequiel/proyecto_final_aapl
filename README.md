# 📈 Financial Portfolio Tracker & Market Analysis

Este proyecto es un sistema de monitoreo financiero automatizado. Utiliza Python para extraer datos en tiempo real de mercados tradicionales (Stock Market) y criptoactivos, procesarlos con Pandas y almacenarlos en una base de datos SQL para su análisis histórico.

## 🚀 Funcionalidades Principales
* **ETL de Finanzas:** Extracción de datos desde Yahoo Finance API y CoinGecko API.
* **Análisis Comparativo:** Normalización de activos (AAPL vs GGAL.BA) para comparar rendimientos porcentuales.
* **Data Wrangling:** Limpieza profunda de datos, manejo de valores nulos (Forward Fill) y aplanamiento de MultiIndex.
* **Persistencia de Datos:** Almacenamiento eficiente en SQLite para consultas rápidas mediante lenguaje SQL.
* **Visualización Avanzada:** Gráficos de precios, medias móviles (MA50) y volatilidad diaria con Matplotlib.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Librerías de Datos:** Pandas, NumPy.
* **Base de Datos:** SQLite3.
* **APIs:** yfinance, Requests (REST APIs).
* **Visualización:** Matplotlib, Seaborn.

## 📊 Roadmap del Proyecto
- [x] Conexión con Yahoo Finance.
- [x] Implementación de base de datos SQL local.
- [x] Consumo de API de Criptomonedas (CoinGecko).
- [ ] Cálculo de Riesgo/Retorno (Ratio de Sharpe).
- [ ] Dashboard interactivo básico.

---
> **Nota:** Este proyecto fue desarrollado como parte de mi formación en análisis de datos, enfocándome en la integridad de los datos y la escalabilidad del código.
