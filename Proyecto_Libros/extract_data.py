#en este archivo debe estar el proceso para extraer y almacenar en el Data Lake sin ninguna transformacion.
from config import GOOGLE_BOOKS_API_KEY
from azure.storage.filedatalake import DataLakeServiceClient