import pandas as pd

class Menu:

    def show_main_menu(self):
        print('\n1: Manage inventory')
        print('2: Inventory Report')

    def show_inventory_menu(self):
        print('\n1: Show all products')
        print('2: Add new product')
        print('3: Remove product')
        print('4: Add inventory of product')
        print('5: Remove inventory of product')

    def show_reports_menu(self):
        print('\n1: Export the current report')
        print('2: Export the report with products to expire')
        print('3: Export the assets balance report')

    def show_coffee_menu(self):
        print('\n1: Derulo Coffee')
        print('2: Comma Coffee')
        print('3: French Coffee')


   

