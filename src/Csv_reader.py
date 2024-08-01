import csv


class CsvReader:
    def read_csv_data(self, file_path: str):
        data = {}
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data[row['id']] = row
        return data