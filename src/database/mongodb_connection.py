from pymongo import MongoClient
from dotenv import load_dotenv
from database_connection import DatabaseConnection
import os

class MongoDBConnection(DatabaseConnection):
    
    def __init__(self):
        # Cargar las variables de entorno
        load_dotenv()
        self.mongo_user = os.getenv('MONGO_USER')
        self.mongo_password = os.getenv('MONGO_PASSWORD')
        self.mongo_host = os.getenv('MONGO_HOST')
        self.mongo_database = os.getenv('MONGO_DATABASE')

        self.client = None
        self.db = None

    def connect(self):
        # Crear la conexión a la base de datos
        conn_string = f'mongodb+srv://{self.mongo_user}:{self.mongo_password}@{self.mongo_host}/{self.mongo_database}?retryWrites=true&w=majority'
        self.client = MongoClient(conn_string)
        self.db = self.client[self.mongo_database]
        print(f"Connected to MongoDB database: {self.mongo_database}")
    
    def insert(self, collection_name, data):
        """Insertar un registro en una tabla de la base de datos."""
        collection = self.db[collection_name]
        collection.insert_one(data)
        print(f"Data inserted into collection {collection_name}")

    def read(self, collection_name, query):
        """Leer datos a través de una consulta SQL."""
        collection = self.db[collection_name]
        return collection.find(query)

    def execute_query(self, query):
        """Ejecutar cualquier consulta SQL."""
        return self.db.command(query)
