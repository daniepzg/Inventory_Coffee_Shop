
from Data_adapters import DataAdapter


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Connector(Singleton):

    def __init__(self, adapter: DataAdapter, path):
        self.path = path
        self.adapter = adapter

    def load_file(self):
            products = self.adapter.read_data(self.path)
            return products

    def save_file(self, products):
        self.adapter.save_data(self.path,products)

