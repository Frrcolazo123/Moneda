import requests
from bs4 import BeautifulSoup
from src.models.Database import Database
import json
import logging
from datetime import datetime
from src.Utils.logger import setup_logger

#Llamo al logger
logger = setup_logger()

class Monitor:                                               #Creo la clase del monito del cambio
    def __init__(self, archivo_config_json):                 #Creo el iniciador con el archivo .json
        with open(archivo_config_json, 'r') as file:         #Accedo al archivo .json para acceder a la ruta y base de datos                       
            self.config = json.load(file)
        self.db = Database(archivo_config_json)

    def obtener_cambio(self):                                #Funcion para obtener el valor del cambio de la pagina web
        try:
            url = self.config['url']
            page = requests.get(url)
            page.raise_for_status()
            soup = BeautifulSoup(page.content, 'html.parser')

            #Accedo al elemento de la clase rate-to del tipo span
            elemento_span = soup.find('span', class_='rate-to')

            if elemento_span:
                valor_tipo_de_cambio = elemento_span.text.strip().split(" ")         #Lo divido en el espacio y corto
                cambio = valor_tipo_de_cambio[0].replace(',', '.')                   #Reemplazo la coma por el punto del valor numerico en posición 0
                logger.info(f"Tipo de cambio obtenido: {cambio}")                   #Cargo el mensaje de la accion en el logger
                return cambio
            else:
                logger.error("No se encontró el elemento con el tipo de cambio en la página")    #Cargo el mensaje de la accion en el logger
                return None
        except requests.RequestException as e:
            logger.error(f"Error al obtener el tipo de cambio: {e}")                             #Cargo el mensaje de la accion en el logger
            return None

    def guardar_en_la_base(self):                                #Funcion para guardar el valor en la tabla currency de la abse de datos cambio
        cambio = self.obtener_cambio()
        if cambio:
            usa = "USD"
            mx = "MXN"
            hoy = datetime.now().strftime('%Y-%m-%d')
            self.db.ingresar_en_la_base(usa, mx, cambio, hoy)        #Llamo a la funcion insert_exchange_rate de la base de datos y les paso sus parametrospip