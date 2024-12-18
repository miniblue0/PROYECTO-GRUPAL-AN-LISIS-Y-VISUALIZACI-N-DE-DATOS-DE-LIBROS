import pyodbc
import os
from config import SQL_SERVER_CONNECTION
import json
from datetime import datetime

def convert_to_date(published_date):
    if not published_date:
        return None  #si la fecha esta vacia o es none, retorna none
    
    #print(f"Intentando convertir la fecha: {published_date}")
    try:
        #primero intento formatearlo como'YYY-MM-DD'
        return datetime.strptime(published_date, '%Y-%m-%d').date()
    except ValueError:
        try:
            return datetime.strptime(published_date + '-01', '%Y-%m-%d').date() #si solo tiene mes y año le agrego un 01
        except ValueError:
            print(f"Error al convertir la fecha: {published_date}") #si no se pudo formatear lo dejo como none
            return None

def load_to_sql_server(data, table_name, connection): 
    print(f"Preparando para cargar {len(data)} libros a la base de datos...")
    
    try:
        conn = pyodbc.connect(connection)
        cursor = conn.cursor()

        for row in data:
            published_date = convert_to_date(row['published_date']) if row['published_date'] else None
            if not published_date:
                print(f"Fecha invalida en el libro {row['title']}. Se omite el registro.")
                continue

            #depuro para ver las fechas
            #print(f"Fecha convertida para '{row['title']}': {published_date}")

            #si la fecha es valida ejecuta la query
            UPSERT = f"""
            MERGE {table_name} AS target
            USING (SELECT ? AS title, ? AS authors, ? AS published_date, ? AS popularity, 
                          ? AS popularity_category, ? AS description) AS source
            ON target.title = source.title
            WHEN MATCHED THEN
                UPDATE SET 
                    title = source.title,
                    authors = source.authors,
                    published_date = source.published_date,
                    popularity = source.popularity,
                    popularity_category = source.popularity_category,
                    description = source.description
            WHEN NOT MATCHED THEN
                INSERT (title, authors, published_date, popularity, popularity_category, description)
                VALUES (source.title, source.authors, source.published_date, 
                        source.popularity, source.popularity_category, source.description);
            """

            cursor.execute(
                UPSERT,
                row['title'],
                ', '.join(row['authors']) if row['authors'] else None,
                published_date,
                row['popularity'],
                row['popularity_category'],
                row['description']
            )

        conn.commit()
        print(f"Datos cargados correctamente en la tabla '{table_name}'.")

    except Exception as e:
        print(f"Error al cargar datos en SQL Server: {e}")
    finally:
        if 'conn' in locals(): #si se pudo conectar cierra la coneccion, sino no
            conn.close()

if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.abspath(__file__))
    transformed_file = os.path.join(project_dir, "transformed_books.json")

    with open(transformed_file, "r") as f:
        transformed_data = json.load(f)

    table_name = "books_popularity"
    load_to_sql_server(transformed_data, table_name, SQL_SERVER_CONNECTION)
