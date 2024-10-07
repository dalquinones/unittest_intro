# Calculator tests

Este proyceto muestra un código simple de calculadora en python que guarda registros en un archivo de texto.


## Instalación

Recuerda descargar python `3.10` o mayor

1. Clonar el repositorio
2. instalar dependencias con `pip install -r requirements.txt`

## Ejercicio

1. Crear y ejecutar los tests unitarios para cada funcion

* Usando unittest: 
    1. `python -m unittest -v dicover tests/` Para ejecutar todos los tests en una carpeta.
    2. `python -m unittest tests/<nombre_del_archivo>` Para ejecutar los tests en un archivo.
* Usando pytest:
    1. `pytest tests/<nombre_del_archivo>` Para ejecutar todos los tests en una carpeta.
    2. `pytest tests/<nombre_del_archivo>::<nombre_de_la_clase>::<nombre_del_test>` Para ejecutar un test en específico.

2. Usar `setup` y `teardown` para definir variables globales y para limpiar la creación del archivo log de pruebas.

3. Usar `coverage` para generar un reporte de cobertura de pruebas

    * `coverage run -m unittest discover` para guardar un reporte en memoria de todo nuestro código.
    * `coverage report` Para guardar el reporte en el proyecto.
    * `coverage html` para generar una carpeta que nos permite ver el reporte en una página web.

