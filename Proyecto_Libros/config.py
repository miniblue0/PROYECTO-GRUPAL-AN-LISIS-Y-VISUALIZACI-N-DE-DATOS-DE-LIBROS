#config.py
import os
from dotenv import load_dotenv

#Cargar las variables de entorno desde el archivo .env
load_dotenv()

#Obtengo las credenciales desde las variables de entorno

#Credenciales de AWS
AWS_ACCESS_KEY_ID = os.getenv("SECRET_ID_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("BUCKET_NAME")

#Credenciales de la api
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

#Credenciales de la base de datos
SQL_SERVER_CONNECTION_STRING = os.getenv("SQL_SERVER_CONNECTION_STRING")
