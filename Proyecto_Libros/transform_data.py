#en este archivo solo debe ir el proceso para transformar los datos recibidos de la api
#categorizando la popularidad en ALTA, MEDIA y BAJA. (si pueden hacerlo con porcentaje mejor :)   )
import pandas as pd
import json
import os

#transformacion de los datos
def transform_data(raw_path):
    with open(raw_path, 'r') as f:
        books = json.load(f)

    datos_transformados = []

    for item in books:
        volume_info = item.get("volumeInfo", {})
        popularidad_categoria = volume_info.get("ratingsCount")

        #arma la categoria de popularidad
        if popularidad_categoria is not None:
            PromPopularidad = (popularidad_categoria / 5) * 100
            if PromPopularidad >= 80:
                PromPopularidad = "ALTA"
            elif PromPopularidad >= 40:
                PromPopularidad = "MEDIA"
            else:
                PromPopularidad = "BAJA"
        else:
            PromPopularidad = "BAJA"

        #arma el diccionario ya transformado
        datos_transformados.append({
            "id": item.get("id").lower(),
            "title": volume_info.get("title"),
            "authors": volume_info.get("authors"),
            "published_date": volume_info.get("publishedDate"),
            "popularity": volume_info.get("averageRating"),
            "description": volume_info.get("description"),
            "popularity_category": PromPopularidad  
        })

    df = pd.DataFrame(datos_transformados)
    print(df)
    return datos_transformados


#cargo la ruta actual 
project_dir = os.path.dirname(os.path.abspath(__file__))
    
#ruta al json con los datos en crudo 
raw_path = os.path.join(project_dir, "raw_books.json")


transform_data(raw_path)