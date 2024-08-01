import csv
import json

import pandas as pd
from abc import ABC, abstractmethod


class DataAdapter(ABC):
    @abstractmethod
    def read_data(self, file_path:str) -> dict:
        pass

    def save_data(self, file_path:str, data) -> None:
        pass


class CsvAdapter(DataAdapter):

    def read_data(self, file_path: str) -> dict:
        data = pd.read_csv(file_path)
        columns = ['Cod','Type','Product Name','Price','Description','Quantity']
        data = data[columns]
        return data

    def save_data(self, file_path: str, data) -> None:
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)


class PickleAdapter(DataAdapter):

    def read_data(self, file_path: str) -> dict:
        data = pd.read_pickle(file_path)
        columns = ['Cod','Type','Product Name','Price','Description','Quantity']
        data = data[columns]
        return data

    def save_file(self,file_path: str,  products):
        products.to_pickle(file_path, index=False)


class JsonAdapter(DataAdapter):

    def read_data(self, file_path: str) -> dict:
        columns = ['Cod','Type','Product Name','Price','Description','Quantity']
        df = pd.read_json(file_path)
        df= df[columns]
        return df

    def save_data(self, file_path: str, data) -> None:
        df = pd.DataFrame(data)
        df.to_json(file_path, orient='records')