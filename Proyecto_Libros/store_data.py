#en este archivo solo debe ir el proceso para almacenar los datos transformados en sql server.
'''la tabla puede tener por ejemplo: id, title, authors, publishedDate, popularity , description, popularity_category 
'''

import pyodbc
import requests
import os
from dotenv import load_dotenv

load_dotenv('C:\\Users\\Soraya\\Desktop\\Tommy\\CSE_110\\books_project\\PROYECTO-GRUPAL-ANALISIS-Y-VISUALIZACION-DE-DATOS-DE-LIBROS\\Proyecto_Libros\\env_variables.env')

api_key = os.getenv('API_KEY')
uid = os.getenv('SQL_USER')
pwd = os.getenv('SQL_PWD')
driver = os.getenv('DRIVER')


#Se establece la conexión con el servidor
conn = pyodbc.connect(f'DRIVER={driver};SERVER=.\SQLEXPRESS;DATABASE=books_db;UID={uid};PWD={pwd}')

#Este print es sólo para debug
print('conexión establecida')

#Se crea un cursor para ejecutar consultas SQL
cursor = conn.cursor()

#Consulta que se va a ejecutar
query = """
IF NOT EXISTS(SELECT 1 FROM books WHERE title = ? AND authors = ?)
BEGIN
    INSERT INTO books(title, authors, publishedDate, popularity, description, popularity_category)
    VALUES(?, ?, ?, ?, ?, ?)
END
ELSE
BEGIN
    UPDATE books (popularity, description, popularity_category)
    SET (?, ?, ?)
END
"""

#Se ejecuta el código:
cursor.execute(query, )

#Se guardan los cambios y se cierra la conexión
conn.commit()
conn.close()