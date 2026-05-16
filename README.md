# 📈 Financial ETL Pipeline & Market Analytics Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data_Wrangling-indigo?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/SQLite3-SQL_Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite3">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
</p>

---

## 🚀 Descripción del Proyecto

Este proyecto es un **Pipeline de Datos (ETL) automatizado** diseñado bajo estándares profesionales de desarrollo de software. El sistema extrae datos financieros en tiempo real desde mercados globales, los procesa y limpia mediante programación modular en capas, los almacena de forma eficiente en una base de datos relacional local (`SQL`) y los expone de manera dinámica en un **Dashboard Interactivo**.

Ideal para centralizar la información de activos y tomar decisiones basadas en datos de tendencia y volatilidad histórica.

---

## 🛠️ Stack Tecnológico

| Componente | Herramientas Utilizadas |
| :--- | :--- |
| **Lenguaje Core** | Python 3.x |
| **Extracción (API)** | Yahoo Finance API (`yfinance`) |
| **Data Wrangling** | Pandas, NumPy |
| **Almacenamiento** | SQLite3 (Motor SQL embebido) |
| **Interfaz & Dashboard**| Streamlit |
| **Visualización** | Matplotlib, Seaborn |

---

## 📁 Arquitectura y Modularización del Código

A diferencia de un script suelto en un Notebook, este desarrollo implementa **programación modular** separando las responsabilidades del pipeline en capas independientes para garantizar su escalabilidad:

```text
proyecto_final_finanzas/
│
├── data/                    # Persistencia de Datos
│   └── finanzas.db          # Base de datos relacional (SQLite)
│
├── scripts/                 # Capas del Proceso ETL (Módulos .py)
│   ├── extract.py           # Extracción y aplanamiento de MultiIndex de la API
│   ├── transform.py         # Limpieza profunda, manejo de nulos y cálculo de KPIs
│   └── load.py              # Carga e inyección de datos estructurados en SQL
│
├── main.py                  # Orquestador del Pipeline Completo
├── app.py                   # Aplicación Web Interactiva (Dashboard)
├── requeriments.txt         # Gestión de dependencias
└── README.md                # Documentación del proyecto