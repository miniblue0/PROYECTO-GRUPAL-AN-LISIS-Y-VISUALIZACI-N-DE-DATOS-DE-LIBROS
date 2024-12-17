#en este archivo debe estar el proceso para extraer y almacenar en UN JSON sin ninguna transformacion.
#from azure.storage.filedatalake import DataLakeServiceClient
import requests
import json
from config import GOOGLE_BOOKS_API_KEY


##hago la peticion de siempre a la api pero use un maximo de libros (para poder ver mejor los datos) si cambian max_results les devuelve mas o menos libros
def extract_data(query = 'book', max_results = 1):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={GOOGLE_BOOKS_API_KEY}&maxResults={max_results}"
    response = requests.get(url)
    if response.status_code == 200:
        books_data = response.json().get("items", [])
        print(f"Se obtuvieron {len(books_data)} libros.")
        return books_data
    else:
        raise Exception(f"Error al obtener datos: {response.status_code}")



##ahora guardo los libros en un archivo json aparte para luego subirlo al dataLake
def save_raw_data(books_data, output_path):
    with open(output_path, 'w') as f:
        json.dump(books_data, f, indent=4)
    print(f"Datos crudos guardados en {output_path}")


books = extract_data(query = 'book', max_results = 1)
save_raw_data(books, "Proyecto_Libros/raw_books.json")
