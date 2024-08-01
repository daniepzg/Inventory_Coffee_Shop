import csv
import pickle
from abc import ABC, abstractmethod


class DataAdapter(ABC):
    @abstractmethod
    def read_data(self, file_path:str) -> dict:
        pass


class CsvAdapter(DataAdapter):

    def read_data(self, file_path: str) -> dict:
        data = {}
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data[row['Cod']] = {
                    'Cod': row['Cod'],
                    'Type': row['Type'],
                    'Product Name': row['Product Name'],
                    'Price': row['Price'],
                    'Description': row['Description'],
                    'Quantity': row['Quantity']
                }
        return data


class PickleAdapter(DataAdapter):

    def read_data(self, file_path: str) -> dict:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)