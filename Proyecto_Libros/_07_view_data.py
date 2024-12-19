#en este archivo solo debe estar el proceso para mostrar los datos, ya sea con pandas, matplotlib o seaborn.

import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
from _02_config import SQL_SERVER_CONNECTION 


def view_data(table, connection):
    try:
        conn = pyodbc.connect(connection)
        print("conectado a la base de datos")
    except Exception as e:
        print(f"error al conectar a la base de datos: {e}")
        return

    #primero uso pandas para guardar los datos en un dataframe y despues eliminar los nulos
    try:
        query = f"SELECT title, popularity FROM {table}"
        df = pd.read_sql(query, conn)
        print("datos extraidos de SQL server.")
    except Exception as e:
        print(f"error al consultar los datos: {e}")
        return
    finally:
        conn.close()
        print("conexion cerrada")

    try:
        #print(df.head())
        #cambio los valores desconocidos
        def convert_popularity(value):
            if value == "Desconocida":
                return 0  #cambia 'Desconocida' con 0
            try:
                return float(value) #conviertea float, sino devuelve 0
            except ValueError:
                return 0  

        df['popularity'] = df['popularity'].apply(convert_popularity)
        df = df[df['popularity'] != 0]
        if df.empty:
            print("el dataframe esta vacio")
            return
        
        if df['popularity'].sum() == 0:
            print("no hay datos conocidos para graficar")
            return
          


        #df = df.nlargest(20, 'popularity')  
        

    except Exception as e:
        print(f"error al preparar los datos: {e}")
        return

    #visualizar los datos con un grafico de barras
    try:
        #esto lo deje tal cual hizo mario
        plt.figure(figsize=(12, 7))
        plt.bar(df['title'], df['popularity'], color='skyblue')

        plt.title('Popularidad de Libros', fontsize=16)
        plt.xlabel('Título del Libro', fontsize=12)
        plt.ylabel('Popularidad', fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()

        #imprimo el grafico
        print("mostrando el grafico en pantalla...")
        plt.show()

    except Exception as e:
        print(f"error al generar el grafico: {e}")



if __name__ == "__main__":
    table = "books_popularity"
    view_data(table, SQL_SERVER_CONNECTION)
