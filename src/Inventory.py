from abc import ABC, abstractmethod

import pandas as pd
from Adapter_Mgr import Connector
from Logger import LoggerFactory

class Publisher(ABC):
    @abstractmethod
    def register_listener(self, listener):
        pass

    @abstractmethod
    def remove_listener(self, listener):
        pass

    @abstractmethod
    def notify_listeners(self):
        pass

class Inventory:
    def __init__(self,adapter, path):
        self._connection = Connector(adapter,path)
        self.products = self._connection.load_file()
        self.logger = LoggerFactory.create_logger('file')
        self.notifier = Notifier()
        self.notifier.register_listener(self.logger)



    def show_All_Products(self):
        print(self.products.to_string())
        msg ='All products have been shown'
        self.notifier.notify_listeners('info', msg)

    def show_Product_Types(self):
        products_type = self.products['Type'].unique()
        for idx, prod in enumerate(products_type):
            print(f'{idx + 1}: {prod}')
        return products_type
    

    def add_new_product(self, product):
        if product.product_name not in self.products:
            product.cod = len(self.products) + 1
            self.products = pd.concat([self.products, product.to_Data_Frame()])
            self._connection.save_file(self.products)
            msg ='A new product has been successfully added to the inventory'
            self.notifier.notify_listeners('info',msg)

    def remove_product(self, cod):
        if cod not in self.products['Cod'].values:
            msg ='Please insert a valid code'
            self.logger.error(msg)
        else:
            self.products = self.products.loc[self.products['Cod'] != cod]
            self._connection.save_file(self.products)
            msg ='Product has been removed from the inventory'
            self.notifier.notify_listeners('warning',msg)

    def add_inventory_of_product(self,cod,quantity):
        quantity = self.products[self.products['Cod'] == cod]['Quantity'] + quantity
        self.products.loc[quantity.index, 'Quantity'] = quantity.values
        self._connection.save_file(self.products)
        msg='Product has been successfully added to the inventory'
        self.notifier.notify_listeners('warning',msg)


    def remove_inventory_of_product(self,cod,quantity):
        current_qty = self.products[self.products['Cod']==cod][['Quantity']]
        if quantity > current_qty.values:
            msg ='Please insert a quantity smaller than the current inventory'
            self.notifier.notify_listeners('error',msg)
        else:
            quantity = self.products[self.products['Cod'] == cod]['Quantity'] - quantity
            self.products.loc[quantity.index, 'Quantity'] = quantity.values
            self._connection.save_file(self.products)
            msg='Product has been removed from the inventory'
            self.notifier.notify_listeners('warning',msg)


class Notifier(Publisher):
    def __init__(self):
        self.listeners = []

    def register_listener(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)
        else:
            print(f'listener {listener} already registered!')

    def remove_listener(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self, log_type, msg):
        for listener in self.listeners:
            if log_type == 'warning':
                listener.warning(msg)
            elif log_type == 'info':
                listener.info(msg)
            else:
                listener.error(msg)