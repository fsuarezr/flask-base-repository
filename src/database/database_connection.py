from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    
    @abstractmethod
    def connect(self):
        """Establishes a connection to the database."""
        pass

    @abstractmethod
    def insert(self, data):
        """Inserts data into the database."""
        pass

    @abstractmethod
    def read(self, query):
        """Reads data from the database."""
        pass

    @abstractmethod
    def execute_query(self, query):
        """Executes a raw query in the database."""
        pass
