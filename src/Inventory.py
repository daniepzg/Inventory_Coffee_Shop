import pandas as pd
from Connector_class import Connector
from Logger import LoggerFactory


class Inventory:
    def __init__(self):
        self._connection = Connector()
        self.products = self._connection.load_file()
        self.logger = LoggerFactory.create_logger('file')


    def show_All_Products(self):
        print(self.products.to_string())

    def show_Product_Types(self):
        products_type = self.products['Type'].unique()
        for idx, prod in enumerate(products_type):
            print(f'{idx + 1}: {prod}')
        return products_type
    

    def add_new_product(self, product):
        if product.product_name not in self.products:
            product.cod = len(self.products) + 1
            self.products = pd.concat([self.products, product.to_Data_Frame()])
            self.connection.save_file(self.products)
            print(f'{product.quantity} pieces of the product {product.product_name} has been successfully added to the inventory')

    def remove_product(self, cod):
        if cod not in self.products['Cod']:
            print('Please insert a valid code')
        else:
            self.products = self.products.loc[self.products['Cod'] != cod]
            self.connection.save_file(self.products)

    def add_inventory_of_product(self,cod,quantity):
        quantity = self.products[self.products['Cod'] == cod]['Quantity'] + quantity
        self.products.loc[quantity.index, 'Quantity'] = quantity.values
        self.connection.save_file(self.products)
        print(f'{quantity} pieces have been added to the inventary of the product with code {cod}.')


    def remove_inventory_of_product(self,cod,quantity):
        current_qty = self.products[self.products['Cod']==cod][['Quantity']]
        if quantity > current_qty.values:
            msg ='Please insert a quantity less than the current inventory {current_qty.values}'
            self.logger.warning(msg)


        else:
            quantity = self.products[self.products['Cod'] == cod]['Quantity'] - quantity
            self.products.loc[quantity.index, 'Quantity'] = quantity.values
            self.connection.save_file(self.products)
            print(f'{quantity} pieces have been removed from the inventary of the product with code {cod}.')
