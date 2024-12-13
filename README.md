# PROYECTO GRUPAL: ANÁLISIS Y VISUALIZACIÓN DE DATOS DE LIBROS
## Les dejo una breve explicacion para que puedan clonar este repositorio y crear sus ramas de trabajo.

### Flujo de Trabajo

-  Clonar el Repositorio
    Para comenzar a trabajar en el proyecto, clona el repositorio ejecutando el siguiente comando en tu terminal: 
    ```bash
    git clone https://github.com/miniblue0/PROYECTO-GRUPAL-ANALISIS-Y-VISUALIZACION-DE-DATOS-DE-LIBROS.git
    ```
    Luego, entra en el directorio del repositorio:
    ```bash
    cd PROYECTO-GRUPAL-ANALISIS-Y-VISUALIZACION-DE-DATOS-DE-LIBROS
    ```

-  Instalación de Dependencias
    Instala las dependencias con el siguiente comando:
    
    ```bash
    pip install -r requirements.txt
    ```

-  Configuracion:
     Crea un archivo .env y configura las credenciales para la API de Google Books, el Data Lake y SQL Server.
     
-  Crear una Nueva Rama de Trabajo
    Es importante que cada uno trabaje en una rama separada. Para crear tu rama:
    
    Asegúrate de estar en la rama main:
    ```bash
    git checkout main
    ```
    Actualiza tu repositorio local:
    ```bash
    git pull origin main
    ```
    Crea una nueva rama con un nombre descriptivo:
    ```bash
    git checkout -b nombre-de-tu-rama
    ```
    Reemplaza nombre-de-tu-rama con su parte del trabajo que va a hacer y la persona encargada. ej: 
    ```bash
    git checkout -b mario-extraer
    ```
-  Hacer Cambios y Confirmarlos (Commit)
    Cuando hayas realizado cambios en los archivos del proyecto, agrégalos al área de preparación y haz el commit:
    
    Agrega todos los archivos modificados al área de preparación:
    ```bash
    git add .
    ```
    Realiza el commit con un mensaje:
    ```bash
    git commit -m "Descripción clara de los cambios realizados"
    ```
    - 6. Subir los Cambios al Repositorio Remoto
    Para subir los cambios a tu rama en el repositorio remoto, ejecuta:
    ```bash
    git push origin nombre-de-tu-rama
    ```

-  Crear una Pull Request (PR)
    Una vez que hayas terminado tu trabajo y subido todos los cambios:
    
    Ve a la página del repositorio en GitHub y entra en tu rama de trabajo.
    Verás un botón que sugiere crear una Pull Request para la rama que acabas de subir. Haz clic en "Compare & pull request".
    Escribe un título y una descripción detallada sobre los cambios realizados.
    Haz clic en "Create Pull Request".

-  Revisión y Fusión de la Pull Request
    Yo voy a revisar la Pull Request para probar el codigo y asegurarme que todo esté implementado correctamente.
    Si todo está bien, fusionaré la PR con la rama main.

-  Actualizar tu Rama Local con los Cambios de main
    Después de que se fusione una Pull Request tienen que actualizar su repositorio local con los nuevos cambios:
    
    Asegúrate de estar en la rama main:
    ```bash
    git checkout main
    ```
    Actualiza tu rama main local:
    ```bash
    git pull origin main
    ```
