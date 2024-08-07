import psycopg2
import json
import logging
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



class Database:
    def __init__(self, config_file):
        self.db_config = None  # Inicializa db_config como None al inicio
        self.conn = None  # Inicializa conn como None al inicio
        self.cargar_configuracion(config_file)  # Carga la configuración del archivo

        # Intenta conectar a la base de datos
        try:
            self.conectar_base_de_datos()
            logging.info("Conexión a la base de datos establecida")
        except psycopg2.OperationalError as e:
            logging.error(f"Error al conectar a la base de datos: {e}")
            raise  # Lanza el error para terminar la ejecución si la conexión falla

    def cargar_configuracion(self, config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)
            self.db_config = config['database']

    def conectar_base_de_datos(self):
        # Conexión a la base de datos predeterminada 'postgres' para crear la base de datos principal
        conn = psycopg2.connect(
            host=self.db_config['host'],
            port=self.db_config['port'],
            user=self.db_config['user'],
            password=self.db_config['password'],
            dbname='postgres'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Verifica si la base de datos especificada existe
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{self.db_config['dbname']}'")
        exists = cursor.fetchone()

        if not exists:
            # Crea la base de datos si no existe
            cursor.execute(f"CREATE DATABASE {self.db_config['dbname']}")
            logging.info(f"La base de datos '{self.db_config['dbname']}' ha sido creada.")
        else:
            logging.info(f"La base de datos '{self.db_config['dbname']}' ya existe.")

        cursor.close()
        conn.close()

        # Ahora establecemos la conexión a la base de datos real
        self.conn = psycopg2.connect(
            host=self.db_config['host'],
            port=self.db_config['port'],
            user=self.db_config['user'],
            password=self.db_config['password'],
            dbname=self.db_config['dbname']
        )
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    def crear_tabla(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS currency (
                    id SERIAL PRIMARY KEY,
                    fromcurrency VARCHAR(3),
                    tocurrency VARCHAR(3),
                    total_value DOUBLE PRECISION,
                    storeday DATE
                )
            """)
            self.conn.commit()
            cursor.close()
            logging.info("La tabla 'currency' fue creada en la base de datos si no existía")
        except Exception as e:
            logging.error(f"Error al crear la tabla: {e}")

    def ingresar_en_la_base(self, usa, mx, cambio, hoy):
        self.crear_tabla()
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO currency (fromcurrency, tocurrency, total_value, storeday) VALUES (%s, %s, %s, %s)",
                (usa, mx, cambio, hoy)
            )
            self.conn.commit()
            cursor.close()
            logging.info(f"Tipo de cambio insertado: {usa} a {mx}, valor: {cambio}, fecha: {hoy}")
        except Exception as e:
            logging.error(f"Error al insertar el tipo de cambio: {e}")
