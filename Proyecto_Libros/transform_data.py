import requests
import os
import json
import pandas as pd
from dotenv import load_dotenv


#transformacion de los datos
def transform_data(raw_path):
    with open(raw_path, 'r') as f:
        books = json.load(f)
    
    datos_transformados = []

    #transformacion de los datos
    for iten in books:
        volume_info=iten.get("volumeInfo",{})  #si no hay volumeInfo, se le asigna un diccionario vacio
        popularidad_categoria=volume_info.get("ratingsCount")
        #categorizacion de la popularidad
        if popularidad_categoria is not None:
            PromPolularidad=(popularidad_categoria/5)*100
            if PromPolularidad >= 80:
                PromPopularidad="ALTA"
            elif PromPolularidad >= 40:
                PromPopularidad="MEDIA"
            else:
                PromPopularidad="BAJA"
        else:
            PromPopularidad="BAJA" #si no hay popularidad, se le asigna BAJA

        datos_transformados.append({
            "id":iten.get("id").lower(),
            "title":volume_info.get("title"),
            "authors":volume_info.get("authors"),
            "publishedDate":volume_info.get("publishedDate"),
            "popularity":volume_info.get("averageRating"),
            "description":volume_info.get("description"),
            "popularity_category":PromPopularidad
        })
    df = pd.DataFrame(datos_transformados)
    print(df)
    return datos_transformados
#cargo la ruta actual 
project_dir = os.path.dirname(os.path.abspath(__file__))
#ruta al json con los datos en crudo 
raw_path = os.path.join(project_dir, "raw_books.json")
transform_data(raw_path)

#en este archivo solo debe ir el proceso para transformar los datos recibidos de la api

#categorizando la popularidad en ALTA, MEDIA y BAJA. (si pueden hacerlo con porcentaje mejor)
