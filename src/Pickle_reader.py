import pickle

class PickleReader:
    def read_pickle_data(self, file_path: str):
        # Read the pickle file
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data