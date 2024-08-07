import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.Monitor import Monitor


def main():
    
    archivo_json = 'src/config/config.json'
    monitor = Monitor(archivo_json)
    monitor.guardar_en_la_base()

if __name__ == "__main__":
    main()