#en este archivo solo debe ir el proceso para almacenar los datos transformados en sql server.

#la tabla puede tener por ejemplo: id, title, authors, publishedDate, popularity , description, popularity_category

#-----------------------------------------------

# Hasta ahora no pude poner a prueba el código, tuve dificultades
# para obtener los datos, asi que si al probarlo algo sale mal
# seguramente tenga que ver con eso...

#-----------------------------------------------

#Importando dependencias
import pyodbc
import requests
import os
from dotenv import load_dotenv


# Cargando variables de entorno (Desafortunadamente sólo conseguí hacerlo al introducir
# toda la ruta local hasta el archivo .env)
load_dotenv('C:\\Users\\Soraya\\Desktop\\Tommy\\CSE_110\\books_project\\PROYECTO-GRUPAL-ANALISIS-Y-VISUALIZACION-DE-DATOS-DE-LIBROS\\Proyecto_Libros\\env_variables.env')

# Obteniendo valores del archivo .env
uid = os.getenv('SQL_USER')
pwd = os.getenv('SQL_PWD')
driver = os.getenv('DRIVER')

# Parámetros de la función:
# driver = El driver del motor SQL
# server = El servidor SQL
# database = La base de datos que se va a usar en la consulta
# table = La tabla en la que se insertarán los datos
# user = Usario con permisos en la base de datos
# password = Contraseña del ususario para conectarse al servidor
# data = La lista con los datos transformados que se van a cargar

def upload_to_sql(driver, server, database, table, user, password, data):

    try:
        print(f'Estableciendo conexión con el servidor {server}')

        #Se establece la conexión con el servidor y la base de datos en SQL
        conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}')

        print('conexión establecida exitosamente')

        #Se itera sobre cada elemento de la lista (cada libro) y se extraen cada uno de
        #los valores de las columnas en un string separados por comas (de esta manera
        # los datos pueden ser incluidos en una sentencia INSERT para que SQL pueda
        # guardarlos en una tabla temporal que se usará más adelante)
        values = ', '.join(f"({book['title']}, {book['authors']}, {book['publishedDate']}, {book['popularity']}, {book['description']}, {book['popularity_category']})" for book in data
        )
        
        #Se crea un cursor para ejecutar consultas SQL en la conexión
        cursor = conn.cursor()

        #Consulta que se va a ejecutar:
        #Se crea una tabla temporal (#new_books), dentro de la cual se insertan los
        #datos actualizados de los libros (guardados en la variable values).
        #Luego, esta tabla temporal se une con la tabla de destino de los datos a
        #través de un MERGE, de modo que se pueden mantener datos actualizados
        #insertando los nuevos, actualizando los viejos y eliminando los obsoletos.
        query = f"""
        CREATE TABLE #new_books (
            id int PRIMARY KEY IDENTITY(1,1),
            title varchar(70),
            authors varchar(70),
            publishedDate date,
            popularity decimal(10,2),
            description varchar(100),
            popularity_category varchar(10)
        )

        INSERT INTO #new_books (title, authors, publishedDate, popularity, description, popularity_category)
        VALUES {values};

        MERGE {table} AS TARGET
        USING #new_books AS SOURCE
        ON TARGET.title = SOURCE.title AND TARGET.authors = SOURCE.authors
        WHEN MATCHED THEN
            UPDATE SET
                TARGET.popularity = SOURCE.popularity
                TARGET.description = SOURCE.description
                TARGET.popularity_category = SOURCE.popularity_category
        WHEN NOT MATCHED BY TARGET THEN
            INSERT (title, authors, publishedDate, popularity, description, popularity_category)
            VALUES (SOURCE.title, SOURCE.authors, SOURCE.publishedDate, SOURCE.popularity, SOURCE.description, SOURCE.popularity_category)
        WHEN NOT MATCHED BY SOURCE THEN
            DELETE;
        """

        print('Ejecutando consulta SQL')

        #Se ejecuta la consulta con todos los valores requeridos:
        cursor.execute(query)
        
        #Se guardan los cambios y se cierra la conexión
        conn.commit()
        print('Cambios guardados')
        
    except Exception as e:
        print(f'Error: {e}')

    finally:
        conn.close()
        print('Conexión cerrada')