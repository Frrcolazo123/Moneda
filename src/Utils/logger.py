import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',      #Formato del mensaje
        handlers=[
            logging.FileHandler('src/logs/monitor.log'),    #Guardar el mensaje en el archivo.log
            logging.StreamHandler()])  
    return logging.getLogger(__name__)