import psycopg2
from dotenv import load_dotenv
from database_connection import DatabaseConnection
import os

class PostgresConnection(DatabaseConnection):

    def __init__(self):
        # Cargar las variables de entorno
        load_dotenv()
        self.postgres_host = os.getenv('POSTGRES_HOST')
        self.postgres_db = os.getenv('POSTGRES_DB')
        self.postgres_user = os.getenv('POSTGRES_USER')
        self.postgres_password = os.getenv('POSTGRES_PASSWORD')

        self.connection = None
    
    def connect(self):
        # Crear la conexión a la base de datos
        self.connection = psycopg2.connect(
            host=self.postgres_host,
            database=self.postgres_db,
            user=self.postgres_user,
            password=self.postgres_password
        )
        print(f"Connected to Postgres database: {self.postgres_db}")

    def insert(self, table_name, data):
        """Insertar un registro en una tabla de la base de datos."""
        cursor = self.connection.cursor()
        # Generamos la consulta usando placeholders para evitar inyecciones SQL
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        cursor.execute(query, tuple(data.values()))
        self.connection.commit()
        cursor.close()
        print(f"Data inserted into table {table_name}")

    def read(self, query):
        """Leer datos a través de una consulta SQL."""
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def execute_query(self, query):
        """Ejecutar cualquier consulta SQL."""
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()
        print(f"Query executed: {query}")
