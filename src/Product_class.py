import pandas as pd


class Product:
    def __init__(self, type, name, price, desc, qty):
        self.cod = 1
        self.type = type
        self.product_name = name
        self.price = price
        self.description = desc
        self.quantity = qty

    def to_Data_Frame(self):
        product = {
            'Cod': self.cod,
            'Type': self.type,
            'Product Name': self.product_name,
            'Price': self.price,
            'Description': self.description,
            'Quantity': self.quantity
        }
        df = pd.DataFrame([product])
        return df
