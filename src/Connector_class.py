import pandas as pd

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Connector(Singleton):

    def __init__(self, path='../Products_inventory/Products_list.pkl'):
        self.path = path

    def load_file(self):
        return pd.read_pickle(self.path)

    def save_file(self, products):
        products.to_pickle(self.path, index=False)
