import pandas as pd
from abc import ABC, abstractmethod
import os

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Connector(Singleton):

    def __init__(self, path='../DB/Products_list.pkl'):
        self.path = path

    def load_file(self):
        return pd.read_pickle(self.path)

    def save_file(self, products):
        products.to_pickle(self.path, index=False)

"""class Adapted_db(ABC)
    @abstractmethod
    def connect_db(self,path="../DB"):
        pass


class Connect_pickle(Adapted_db):

class Connect_csv(Adapted_db):

class Adapter:
    @staticmethod
    def get_connection(self,path="../DB"):
        self.folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataFiles')"""

