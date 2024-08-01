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
                data[row['id']] = {
                    'id': row['id'],
                    'name': row['name'],
                    'age': row['age']
                }
        return data


class PickleAdapter(DataAdapter):

    def read_data(self, file_path: str) -> dict:
        # Read the pickle file
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
