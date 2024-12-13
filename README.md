# PROYECTO GRUPAL: ANÁLISIS Y VISUALIZACIÓN DE DATOS DE LIBROS
## Les dejo una breve explicacion para que puedan clonar este repositorio y crear sus ramas de trabajo.

### Flujo de Trabajo
1. Clonar el Repositorio
Para comenzar a trabajar en el proyecto, clona el repositorio ejecutando el siguiente comando en tu terminal: 
```bash
git clone https://github.com/miniblue0/PROYECTO-GRUPAL-ANALISIS-Y-VISUALIZACION-DE-DATOS-DE-LIBROS.git
```
Luego, entra en el directorio del repositorio:
```bash
cd PROYECTO-GRUPAL-ANALISIS-Y-VISUALIZACION-DE-DATOS-DE-LIBROS
```

2. Crear una Nueva Rama de Trabajo
Es importante que cada miembro del equipo trabaje en una rama separada para evitar conflictos. Para crear tu rama:

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
3. Hacer Cambios y Confirmarlos (Commit)
Cuando hayas realizado cambios en los archivos del proyecto, agrégalos al área de preparación y haz el commit:

Agrega todos los archivos modificados al área de preparación:
```bash
git add .
```
Realiza el commit con un mensaje:
```bash
git commit -m "Descripción clara de los cambios realizados"
```
4. Subir los Cambios al Repositorio Remoto
Para subir los cambios a tu rama en el repositorio remoto, ejecuta:
```bash
git push origin nombre-de-tu-rama
```

5. Crear una Pull Request (PR)
Una vez que hayas terminado tu trabajo y subido todos los cambios:

Ve a la página del repositorio en GitHub y entra en tu rama de trabajo.
Verás un botón que sugiere crear una Pull Request para la rama que acabas de subir. Haz clic en "Compare & pull request".
Escribe un título y una descripción detallada sobre los cambios realizados.
Haz clic en "Create Pull Request".

6. Revisión y Fusión de la Pull Request
Yo voy a revisar la Pull Request para probar el codigo y asegurarme que todo esté implementado correctamente.
Si todo está bien, fusionaré la PR con la rama main.

7. Actualizar tu Rama Local con los Cambios de main
Después de que se fusione una Pull Request tienen que actualizar su repositorio local con los nuevos cambios:

Asegúrate de estar en la rama main:
```bash
git checkout main
```
Actualiza tu rama main local:
```bash
git pull origin main
```
