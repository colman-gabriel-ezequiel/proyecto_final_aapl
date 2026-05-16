import sqlite3

def cargar_en_sql(df, db_path='data/finanzas.db'):
    conexion = sqlite3.connect(db_path)
    # Tu bloque de carga a SQLite
    df.to_sql('activos', conexion, if_exists='replace', index=False)
    conexion.close()
    print(f"Datos guardados en {db_path}")