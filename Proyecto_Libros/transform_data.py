import requests
import os
import json
import pandas as pd
from dotenv import load_dotenv


#transformacion de los datos
def transform_data():
    books = extract_data(query = 'book', max_results = 1)
    datosTransformados = []
    #transformacion de los datos
    for iten in books:
        popularidad_categoria=iten.get("volumeInfo").get("ratingsCount")
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
            PromPopularidad="BAJA"

        datosTransformados.append({
            "id":iten.get("id"),
            "title":iten.get("volumeInfo").get("title"),
            "authors":iten.get("volumeInfo").get("authors"),
            "publishedDate":iten.get("volumeInfo").get("publishedDate"),
            "popularity":iten.get("volumeInfo").get("averageRating"),
            "description":iten.get("volumeInfo").get("description"),
            "popularity_category":popularidad_categoria
        })
    print(pd.DataFrame(datosTransformados))
    return datosTransformados

transform_data()


#en este archivo solo debe ir el proceso para transformar los datos recibidos de la api

#categorizando la popularidad en ALTA, MEDIA y BAJA. (si pueden hacerlo con porcentaje mejor)
