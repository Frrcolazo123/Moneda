#!/bin/bash

# Salir si algún comando falla
set -e

# Crear un entorno virtual
python -m venv venv
source venv/bin/activate

# Actualizar pip y setuptools
pip install --upgrade pip setuptools wheel

# Instalar dependencias necesarias para la construcción del paquete
pip install -r requirements.txt

# Construir el paquete y generar el archivo .whl
python setup.py sdist bdist_wheel