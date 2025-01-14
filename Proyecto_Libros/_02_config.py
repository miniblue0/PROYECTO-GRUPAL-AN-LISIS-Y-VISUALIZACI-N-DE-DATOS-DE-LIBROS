#config.py
import os
from dotenv import load_dotenv

#Cargar las variables de entorno desde el archivo .env
load_dotenv()

#Obtengo las credenciales desde las variables de entorno

#Credenciales de AWS
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

#Credenciales de la api
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

#Credenciales de la base de datos
SQL_SERVER_CONNECTION = os.getenv("SQL_SERVER_CONNECTION")

#40 libros por defecto
MAX_RESULTS = int(os.getenv("MAX_RESULTS", 40))  
