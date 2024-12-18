#en este archivo solo debe estar el proceso para mostrar los datos, ya sea con pandas, matplotlib o seaborn.

#0-Carga las variables del archivo .env usando dotenv.
#1-Establece la conexión a SQL Server usando pyodbc.
#2-Ejecuta la consulta SQL para obtener las columnas title y popularity de la tabla new_books.
#3-Crea un gráfico de barras donde:
#4-Eje X: title → Títulos de los libros.
#5-Eje Y: popularity → Niveles de popularidad.
#6-Muestra el gráfico utilizando Matplotlib.

#AQUI ESTA DETALLADAS LAS LIBRERIAS PERO SE OMITIRAN LAS QUE YA ESTAN INICIALIZADAS

# --> ( pip install matplotlib )

#import os
#import pyodbc
#import pandas as pd
import matplotlib.pyplot as plt
#from dotenv import load_dotenv

def visualize_popularity():
    """
    Función para conectar a SQL Server, leer la tabla 'new_books' 
    y graficar un gráfico de barras con la popularidad de los libros.
    """
    
    # 1. Cargar variables del archivo .env
    load_dotenv()  # Cargar las variables del entorno
    
    DRIVER = os.getenv("driver")
    SERVER = os.getenv("server")
    DATABASE = os.getenv("database")
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    TABLE = "new_books"  # Nombre de la tabla MODIFICAR SI FUERA NECESARIO

    # 2. Establecer la conexión con SQL Server
    try:
        # String de conexión
        connection_string = (
            f"DRIVER={DRIVER};"
            f"SERVER={SERVER};"
            f"DATABASE={DATABASE};"
            f"UID={USER};"
            f"PWD={PASSWORD}"
        )
        # Crear la conexión
        conn = pyodbc.connect(connection_string)
        print(" Conexión exitosa a la base de datos.")
        
    except Exception as e:
        print(f" Error al conectar a la base de datos: {e}")
        return

    # 3. Consultar los datos usando Pandas
    try:
        query = f"SELECT title, popularity FROM {TABLE}"
        df = pd.read_sql(query, conn)  # Leer datos y almacenarlos en un DataFrame
        print(" Datos cargados exitosamente desde SQL Server.")
        
    except Exception as e:
        print(f" Error al consultar los datos: {e}")
        return
    
    finally:
        conn.close()  # Cerrar la conexión
        print(" Conexión cerrada.")

    # 4. PRINCIPAL: Visualizar los datos con un gráfico de barras
    try:
        # Configurar el gráfico
        plt.figure(figsize=(10, 6))  # Tamaño del gráfico

        # Opción 1: Eliminar los titulos que contengan NaN en popularity
        # df = df.dropna(subset=['popularity'])  # Elimina filas con NaN en 'popularity'

        # Opción 2: rellenar las popularidades que tienen valores NaN con 0 (si quiero mostrar aun los Titulos)
        # df['popularity'] = df['popularity'].fillna(0)  # Reemplaza NaN con 0 en 'popularity'

        plt.bar(df['title'], df['popularity'], color='skyblue')  # Gráfico de barras
        
        # Personalizar el gráfico
        plt.title('Popularidad de Libros', fontsize=16)
        plt.xlabel('Título del Libro', fontsize=12)
        plt.ylabel('Popularidad', fontsize=12)
        plt.xticks(rotation=45)  # Rotar las etiquetas si son muy largas
        plt.tight_layout()  # Ajustar márgenes
        
        # Mostrar el gráfico
        print("Mostrando gráfico de barras...📊")
        plt.show()
    
    except Exception as e:
        print(f" Error al generar el gráfico: {e}")




# Ejecutar la función si el script se ejecuta directamente, en todo caso la siguiente instruccion deberia ejecutarse en el programa principal o en ETL.py:

#if __name__ == "__main__":
#    visualize_popularity()
