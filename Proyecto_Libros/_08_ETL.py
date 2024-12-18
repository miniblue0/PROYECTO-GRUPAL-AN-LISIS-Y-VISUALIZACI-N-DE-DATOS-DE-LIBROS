#en este archivo iria el script que llame a todos los anteriores y maneje el flujo de trabajo :3
import os
from _02_config import S3_BUCKET_NAME, SQL_SERVER_CONNECTION, GOOGLE_BOOKS_API_KEY, MAX_RESULTS
from _03_extract_data import extract_data, save_raw_data
from _04_load_to_datalake import upload_to_s3
from _05_transform_data import transform_data
from _06_store_data import load_to_sql_server
from _07_view_data import view_data
#se importan las funciones de los modulos anteriores
import json



def proceso_etl(query, max_results, s3_remote_path):
    try:
        project_dir = os.path.dirname(os.path.abspath(__file__)) #ruta del proyecto
        raw_file_path = os.path.join(project_dir, "raw_books.json") #ruta de los archivos en crudo
        transformed_books_path = os.path.join("Proyecto_Libros", "transformed_books.json") #ruta de los archivos transformados
        with open(transformed_books_path, 'r') as f:
            transformed_books = json.load(f)

        table_name = "books_popularity" 

        print("iniciando extraccion de datos...")
        books_data = extract_data(query=query, max_results=MAX_RESULTS) #extraigo los datos
        save_raw_data(books_data, raw_file_path)#guardo los datos en crudo
        print("Extracción completada")

        
        print("subiendo datos crudos al Data Lake...") 
        upload_to_s3(raw_file_path, S3_BUCKET_NAME, s3_remote_path)#subo los datos crudos al dataLake (amazon S3)
        print("datos crudos subidos al Data Lake")        

        
        print("iniciando transformacion de datos...")
        transform_data(raw_file_path, transformed_books_path) #se transforman los datos
        print("transformacion completada")


        print("iniciando carga de datos a SQL server...")
        load_to_sql_server(transformed_books, table_name, SQL_SERVER_CONNECTION) #se cargan a sql 
        print("carga de datos a SQL server completada.")
        
        ###
        print("iniciando la creacion de la vista de popularidad..")
        view_data(table_name, SQL_SERVER_CONNECTION) #se genera la vista 
        print("proceso terminado")

    except Exception as e:

        print(f"error en el proceso ETL: {e}")


if __name__ == "__main__":
    query = "books"
    max_results = 80
    s3_remote_path = "raw_data/raw_books.json" #es la ruta que hay dentro del bucket

    proceso_etl(query, max_results, s3_remote_path)