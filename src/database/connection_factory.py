# connection_factory.py
import os
from mongodb_connection import MongoDBConnection
from postgres_connection import PostgresConnection

def get_database_connection():
    db_type = os.getenv('DB_TYPE')
    
    if db_type == 'mongodb':
        return MongoDBConnection()
    elif db_type == 'postgres':
        return PostgresConnection()
    else:
        raise ValueError(f"Unsupported database type: {db_type}")
