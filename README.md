# okdoc backend en Django

Para poner este backend a andar:

1. `git clone` del repo si no lo tenes, o `git pull`.
2. Crear un virtual environment, `python -m venv <directory>`, siendo \<directory> el nombre del directorio para el environment (puede ser `venv`).
3. El archivo `requirements.txt` tiene todos los paquetes necesarios, se instalan haciendo `pip install -r requirements.txt`.
4. La base de datos es (por ahora) simplemente un archivo `db.sqlite3`, hay que copiarlo en el root the repo.
5. En caso de querer probar alguna cosa, haciendo `python manage.py runserver` inicia el servidor en localhost, se puede ir al panel de admin o lo que sea.