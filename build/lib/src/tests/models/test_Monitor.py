#Modelo
import pytest
from pytest_mock import mocker
from src.models.Monitor import Monitor
from src.Utils.logger import setup_logger

def test_obtener_cambio_not_none():
    monitor = Monitor('src/config/config.json')  # Crear una instancia de la clase Monitor
    cambio = monitor.obtener_cambio()  # Llamar al método de instancia
    assert cambio != None

def test_obtener_cambio_tiene_elementos():
    monitor = Monitor('src/config/config.json')  # Crear una instancia de la clase Monitor
    cambio = monitor.obtener_cambio()  # Llamar al método de instancia
    assert len(cambio) > 0

# Configurar el logger para las pruebas
logger = setup_logger()

@pytest.fixture             #Para poder ser usado por otras funciones
def mock_config(mocker):    # Simular el contenido del archivo de config
    
    mock_open = mocker.patch('builtins.open', mocker.mock_open(read_data='{"database": {"host": "localhost", "port": 5432, "dbname": "cambio", "user": "postgres", "password": "fernando"}, "url": "https://www.exchange-rates.org/es/conversor/usd-mxn"}'))  #Simulo la funcion open con un json ficticio
    mock_json_load = mocker.patch('json.load', return_value={"database": {"host": "localhost", "port": 5432, "dbname": "cambio", "user": "postgres", "password": "fernando"}, "url": "https://www.exchange-rates.org/es/conversor/usd-mxn"})   #Simulo la carga y devuelvo un diccionario con la misma estructura que el archivo JSON simulado
    return mock_open, mock_json_load

@pytest.fixture   
def mock_requests_get(mocker):          # Simular la respuesta de la solicitud HTTP

    mock_response = mocker.Mock()       #Creo un objeto mock para poder simular la respuesta
    mock_response.status_code = 200     #Simulo la consicion exitosa con un codigo de estado 200
    mock_response.content = b'<span class="rate-to">19.8659 MXN</span>'   #Simulo el contenido de la respuesta
    mock_requests_get = mocker.patch('requests.get', return_value=mock_response) #Para que me devuelva el mock_response
    return mock_requests_get

def test_obtener_cambio(mock_config, mock_requests_get):     #Es la prueba pasandole la simulacion del mock que debe tomar
    
    monitor = Monitor('src/config/config.json')    # Crear una instancia de Monitor con un archivo de configuración ficticio
    resultado = monitor.obtener_cambio()           # Llamo al método

    assert resultado == '19.8659'