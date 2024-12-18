#en este archivo solo debe ir el proceso para transformar los datos recibidos de la api
#categorizando la popularidad en ALTA, MEDIA y BAJA. (si pueden hacerlo con porcentaje mejor :)   

import pandas as pd
import json
import os

#transformacion de los datos
def transform_data(raw_path, transformed_path):
    with open(raw_path, 'r') as f:
        books_data = json.load(f)
    print(f"Transformando {len(books_data)} libros...")
    try:
        #lee los datos del json con los datos en crudo
        with open(raw_path, 'r') as f:
            books = json.load(f)

        datos_transformados = []

        #transformacion de los datos
        for item in books:
            popularidad_categoria = item.get("volumeInfo", {}).get("ratingsCount")
                
            #categoriza la popularidad
            if popularidad_categoria is not None:
                prom_popularidad = (popularidad_categoria / 5) * 100
                if prom_popularidad >= 80:
                    popularidad_categoria = "ALTA"
                elif prom_popularidad >= 40:
                    popularidad_categoria = "MEDIA"
                else:
                    popularidad_categoria = "BAJA"
            else:
                popularidad_categoria = "BAJA"

            datos_transformados.append({
                "id": item.get("id"),
                "title": item.get("volumeInfo", {}).get("title"),
                "authors": item.get("volumeInfo", {}).get("authors"),
                "published_date": item.get("volumeInfo", {}).get("publishedDate"),
                "popularity": item.get("volumeInfo", {}).get("averageRating"),
                "popularity_category": popularidad_categoria,               
                "description": item.get("volumeInfo", {}).get("description"),
            })


        #print(pd.DataFrame(datos_transformados))

        #guarda los datos transformados en un json
        with open(transformed_path, 'w') as f:
            json.dump(datos_transformados, f, indent=4)
        print(f"Datos transformados guardados en {transformed_path}.")

    except Exception as e:
        print(f"Error al transformar los datos: {e}")



if __name__ == "__main__":
    #cargo la ruta actual del archivo
    project_dir = os.path.dirname(os.path.abspath(__file__))

    raw_path = os.path.join(project_dir, "raw_books.json")#ruta al json con los datos en crudo 

    transformed_path = os.path.join(project_dir, "transformed_books.json") #ruta al nuevo archivo transformado

    transform_data(raw_path, transformed_path)