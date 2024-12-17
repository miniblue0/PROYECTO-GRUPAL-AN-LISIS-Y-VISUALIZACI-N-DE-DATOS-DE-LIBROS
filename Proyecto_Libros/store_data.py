#en este archivo solo debe ir el proceso para almacenar los datos transformados en sql server.

#la tabla puede tener por ejemplo: id, title, authors, publishedDate, popularity , description, popularity_category

import pyodbc
import os
from config import SQL_SERVER_CONNECTION_STRING #importo desde el archivo config las credenciales
import json

def load_to_sql_server(data, table_name, connection_string): #simplifique los parametros usando directamente la url de sql

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        for row in data:
            #reorganice el merge para comparar los datos
            UPSERT = f"""
            MERGE {table_name} AS target
            USING (SELECT ? AS id, ? AS title, ? AS authors, ? AS publishedDate, ? AS popularity, 
                          ? AS description, ? AS popularity_category) AS source
            ON target.id = source.id
            WHEN MATCHED THEN
                UPDATE SET 
                    title = source.title,
                    authors = source.authors,
                    publishedDate = source.publishedDate,
                    popularity = source.popularity,
                    description = source.description,
                    popularity_category = source.popularity_category
            WHEN NOT MATCHED THEN
                INSERT (id, title, authors, publishedDate, popularity, description, popularity_category)
                VALUES (source.id, source.title, source.authors, source.publishedDate, 
                        source.popularity, source.description, source.popularity_category);
            """
            #ejecuta la consulta anterior con los valores de cada fila
            cursor.execute(
                UPSERT,
                row['id'],
                row['title'],
                ', '.join(row['authors']) if row['authors'] else None,
                row['publishedDate'],
                row['popularity'],
                row['description'],
                row['popularity_category']
            )

        #commit para confirmar los cambios
        conn.commit()
        print(f"Datos cargados exitosamente en la tabla '{table_name}'.")

    except Exception as e:
        print(f"Error al cargar datos en SQL Server: {e}")
    finally:
        conn.close()


#ruta al json con los datos transformados (para no tener que usar una tabla temporal como teniamos anteriormente)
project_dir = os.path.dirname(os.path.abspath(__file__))
transformed_file = os.path.join(project_dir, "transformed_books.json")

#leo los datos del archivo
with open(transformed_file, "r") as f:
        transformed_data = json.load(f)

#nombre de la tabla
table_name = "books_popularity"

#ejecuto la carga a sql
load_to_sql_server(transformed_data, table_name, SQL_SERVER_CONNECTION_STRING)
