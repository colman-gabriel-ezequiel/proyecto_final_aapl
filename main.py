from scripts.extract import extraer_datos  
from scripts.transform import transformar_datos  
from scripts.load import cargar_en_sql  
def run_pipeline():  
    ticket = 'AAPL'  
    raw_data = extraer_datos(ticket)  
    cleaned_data = transformar_datos(raw_data)  
    cargar_en_sql(cleaned_data)  
    print("Pipeline ejecutado con exito!")  
if __name__ == "__main__":  
    run_pipeline() 
