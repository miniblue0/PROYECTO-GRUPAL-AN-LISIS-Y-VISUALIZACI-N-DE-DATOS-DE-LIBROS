# config.py
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales desde las variables de entorno
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")
DATALAKE_ACCOUNT_NAME = os.getenv("DATALAKE_ACCOUNT_NAME")
DATALAKE_ACCOUNT_KEY = os.getenv("DATALAKE_ACCOUNT_KEY")
SQL_SERVER_CONNECTION_STRING = os.getenv("SQL_SERVER_CONNECTION_STRING")
