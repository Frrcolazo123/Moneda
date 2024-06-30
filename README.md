# Proyecto de Conversión de Divisas

Este proyecto permite obtener y almacenar el tipo de cambio entre USD y MXN en una base de datos PostgreSQL.

En este link se encuentra la consigna completa: [text](https://drive.google.com/file/d/15-vOtYZdcFa8X3-hfFAU2c88TivHSn28/view?usp=sharing)

## Instalación

1. Clona el repositorio:

git clone https://github.com/Frrcolazo123/Moneda.git


2. Instala las dependencias:

pip install -r requirements.txt

3. Uso del código:

- Primero debemos correr el contenedor de docker en la terminal del proyecto con el comando: <docker-compose up -d>

- Una vez que el contenedor este corriendo verificamos con <docker ps>, recíen ahí podemos correr el codigo principal main.py <python main.py>

- En consola nos aparecerá los mensajes que nos indica que el código corrió de forma correcta y todas las acciones que quedaron guardadas en el log

- Si accedemos a pgAdmin4 del PostgreSQL y vamos a la base de dato creada con el nombre de "moneda" podemos ver que se creó una tabla con el nombre de "currency" y si hacemos una consulta para ver todos los registros (<SELECT * FROM currency>) podemos notar que contamos con un registro el cual posee un ID, de que moneda proviene y cuál moneda va el cambio, el valor del cambio y la fecha del mismo.

- Esto mismo podemos hacerlo cuando quieras y automaticamente se ira guardando el registro en la base de forma incremental.

4. Para realizar los test unitarios debemos ingresar en la consola: <pytest -v> para recorrer todas las pruebas unitarias y visualizar su resultado.

5. Detalles:

- En la carpeta "config" tenemos el archivo .json en donde se encuentra toda la información correspondiente al acceso de la base de datos y la URL
- En la carpeta "logs" tenemos todos la información de todas las ejecuciones del codigo con los errores y casos de exito.
- En la carpeta "modelos" tenemos el código de los dos modelos, el de Monitor y el de Database.
- En la carpeta "test" tenemos el códgo correspondiente a las pruebas unitarias
- En la carpeta "Utils" tenemos el código correspondiente al logger.
- A su vez tenemos un archivo docker-compose.yml el cual es el encargado de crear el contenedor de docker.
- Y por último tenemos un archivo txt con los requerimientos para que el sistema funcione.
