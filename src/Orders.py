import pandas as pd


class Order:
    def __init__(self):
        self.order = pd.DataFrame(columns=['Name','Price', 'Quantity', 'SubTotal'])

    def add_product(self, product):
        print(self.order)

    def remove_product(self):
        print(self.order)

    def show_products(self):
        print(self.order)




