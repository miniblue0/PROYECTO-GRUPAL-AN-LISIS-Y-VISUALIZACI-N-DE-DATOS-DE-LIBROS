#en este archivo debe estar el proceso para extraer y almacenar en UN JSON sin ninguna transformacion.

import requests
import os
import json
from config import GOOGLE_BOOKS_API_KEY, MAX_RESULTS


##hago la peticion de siempre a la api pero use un maximo de libros (para poder ver mejor los datos) si cambian max_results les devuelve mas o menos libros
def extract_data(query = 'book', max_results = MAX_RESULTS):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={GOOGLE_BOOKS_API_KEY}&maxResults={max_results}"
    response = requests.get(url)
    if response.status_code == 200:
        books_data = response.json().get("items", [])
        print(f"Se obtuvieron {max_results} libros.")
        return books_data
    else:
        raise Exception(f"Error al obtener datos: {response.status_code}")



##ahora guardo los libros en un archivo json aparte para luego subirlo al dataLake
def save_raw_data(books_data, output_path):
    with open(output_path, 'w') as f:
        json.dump(books_data, f, indent=4)
    print(f"Datos crudos guardados en {output_path}")


if __name__ == "__main__":
    #uso valores de prueba para ver si funciona
    query = 'book'
    project_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(project_dir, "raw_books.json")

    #extraigo los datos y guardo en un json
    books = extract_data(query=query)
    save_raw_data(books, output_path)
