from Menus import Menu
from Inventory import Inventory
from Product_class import Product
from Reports import Reports


def logo():
    nombre = "INVENTORY COFFEE SHOP"
    longitud = len(nombre) + 10
    print()
    print("#" * longitud)
    print("#    " + nombre + "    #")
    print("#" * longitud)


def main():
    menu = Menu()
    menu.show_main_menu()
    option = input("\nPlease, choose an option:")
    if option == "1":
        inventory = Inventory()
        inv = True
        while(inv):
            menu.show_inventory_menu()
            action = input("\nPlease, choose an option:")
            if action =="1":
                inventory.show_All_Products()
            if action =="2":
                type_product = inventory.show_Product_Types()
                type = int(input("\nPlease choose the number of the type the product:"))
                name=input("Please insert the name of the product")
                price=float(input("Please insert the price of the product"))
                description=input("Please insert a short description of the product")
                qty=int(input("Please insert the quantity of the inventory of the product:"))
                inventory.add_new_product(Product(type_product[type-1], name, price, description, qty))
            if action=="3":
                inventory.show_All_Products()
                code= int(input("Please insert the code of the product:"))   
                inventory.remove_product(code)
                print(f'The product with the code {code} has been removed from the inventory')
            if action=="4":
                inventory.show_All_Products()
                code= int(input("Please insert the code of the product:"))  
                qty= int(input("Please insert the quantity to add to the inventory:"))  
                inventory.add_inventory_of_product(code,qty)
               
            if action=="5":
                inventory.show_All_Products()
                code= int(input("Please insert the code of the product:"))  
                qty= int(input("Please insert the quantity to remove from the inventory:")) 
                inventory.remove_inventory_of_product(code,qty)
            menu_option = input('Would you like to continue in this menu?(Y), or exit (E)?')
            if menu_option.upper() == 'E':
                inv = False

    if option == "2":
        inventory = Inventory()
        report= Reports(inventory.products)
        inv = True
        while(inv):
            menu.show_reports_menu()
            action = input("\nPlease, choose an option:")
            if action =="1":
                report.current_report()

            elif action =="2":
                report.products_to_expire_report()
            elif action =="3":
                report.assets_balance_report()
            menu_option = input('Would you like to continue in this menu?(Y), or go back to the previous menu (E)?')
            if menu_option.upper() == 'E':
                inv = False


if __name__ == "__main__":
    logo()
    main()