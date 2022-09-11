# Prueba Técnica - ConectApps
## Iniciar el proyecto
Hay 2 formas de levantar el proyecto localmente:
1. Utilizando docker y docker compose (ideal para probarlo)
2. Levantandolo desde el host sin docker-compose (más comodo para el desarrollo)

### 1. Con `docker` y `docker-compose`
Como requisitos previos:
- tener instalado docker y docker compose

Iniciar el proyecto con el siguiente comando:
```
docker-compose up -d
```
si todo sale correctamente, deberías tener habilitada la app desde tu browser en `localhost:8023` o, para ver la documentación de los endpoints en `localhost:8023/docs`

### 2. Levantando el proyecto localmente
Como prequisitos necesitas:
- Tener python (recomendado 3.9 pero puede ser 3.7+)
- Tener un entorno virtual activado para el proyecto (recomendado)
- Tener instalado MySQL 8.0 (recomiendo usar docker)

Pasos para levantar el proyecto:

1. Crear un archivo `.env` con la misma estructura de variables que en `.env-example` pero con los valores correctos.
2. Crear una base de datos (schema) con MySQL con el mismo nombre que el usado en el archivo `.env`
3. Instalar las dependencias necesarias:
```pip install -r requirements-dev.txt```
4. Levantar el proyecto:
```python main.py```

Si todo sale bien, tendrás la app levantada en el puerto indicado en el archivo `.env`

Ejemplo de archivo `.env` válido para desarrollo:
```
DB_USER=root
DB_PASS=root
DB_HOST=localhost
DB_PORT=3306
DB_NAME=conectapps_db
```
Tip: levantar una instancia de MySQL 8.0 con la DB ya creada (`conectapps_db`), usuario `root`, contraseña `root` y accesible desde `localhost` en el puerto `3306` puedes ejecutar el siguiente comando (teniendo docker instalado):
```
docker run -p 3306:3306 --name dev-mysql -e MYSQL_DATABASE=conectapps_db -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0
```
