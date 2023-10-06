# okdoc backend en Django

Este repositorio es el backend, hecho en Django. Para correrlo de manera local:

1. Clonar el repositorio en el directorio que quieras:

    ```bash
    git clone https://github.com/ok-doc-proyecto/okdoc-backend.git
    ```

    En caso de querer editarlo o cambiar cualquier cosa de prueba, primero forkear el repositorio y clonar el fork.

2. Crear un virtual environment para asegurarse de tener las mismas dependencias y libraries. Podes hacerlo donde quieras, pero lo mejor es crearlo en el root del repositorio:

    ```bash
    python -m venv <nombre de la carpeta>
    ```

3. El archivo `requirements.txt` tiene todos los paquetes necesarios, se instalan haciendo:

   ```bash
   pip install -r requirements.txt
   ```

4. La base de datos es (por ahora) simplemente [un archivo](https://1drv.ms/u/s!AltpNhfCpMRXg_AIxkkIQXegy9B2fw?e=ANse2J) `db.sqlite3`, hay que copiarlo en la carpeta `project`.
5. Para poner a funcionar el servidor, desde la carpeta `project` correr el siguiente comando:

    ```bash
    python manage.py runserver
    ```
