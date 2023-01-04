'''This Python program is an inventory manager for a Nike warehouse.
A user can store and view data about shoe stock in the warehouse'''

from tabulate import tabulate
from copy import deepcopy

#================== Define Shoe class ===========================
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        '''Returns the cost of the item'''
        return self.cost

    def get_quantity(self):
        '''Returns the quantity in stock of the item'''
        return self.quantity
    
    def update_quantity(self, new_quantity):
        '''Updates the quantity of the item stock, takes the quantity of total inventory after reorder'''
        self.quantity = new_quantity
    
    def update_cost(self, new_cost):
        '''Updates the cost of the item, takes the cost of an individual item'''
        self.cost = new_cost

    def __str__(self):
        '''Returns a string of formatted information for the item'''
        table = [["Product name", self.product], ["Code", self.code], ["Country", self.country],
        ["Cost", f"R{self.cost}"], ["Quantity", self.quantity]]
        item_string = "\n" + tabulate(table, tablefmt="plain")
        return item_string

    def file_string(self):
        '''Formats information and returns as a string to be written in inventory.txt'''
        item_string = f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n"
        return item_string
    
    def edit_quantity(self):
        while True: 
                user_quantity = input("Please enter current quantity in stock: ").strip()
                try:
                    user_quantity = int(user_quantity)
                    if user_quantity < 0:
                        raise ValueError
                    self.update_quantity(user_quantity)
                    break
                except Exception:
                    print("Invalid input. Please enter a whole number.")

    def edit_cost(self):
        while True:
                user_cost = input("Please enter the current cost: ").strip()
                try:
                    user_cost = int(user_cost)
                    if user_cost <= 0:
                        raise ValueError
                    self.update_cost(user_cost)
                    break
                except Exception:
                    print("Invalid input. Please enter a positive number.")
        


#=============Shoe list===========

#shoe_list will be used to store a list of Shoe objects in stock in the warehouse.
shoe_list = []
#order_list will store a list of Shoe objects to order created by the restock function
order_list = []
#sale_list will store a list of Shoe objects to be marked on sale
sale_list = []

#==========Functions outside the class==============
def code_match(search_code, search_list):
    '''This function searches codes for all shoes in list to see if there is a match.
    It returns the index of the match, or if no match is found, it returns -1.'''
    for index, shoe in enumerate(search_list):
        if shoe.code == search_code:
            return index
    return -1

def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    with open("inventory.txt", "r") as inventory_file:
        inventory_file.readline()
        for line in inventory_file:
            data_list = line.strip().split(",")
            try:
                new_shoe = Shoe(data_list[0], data_list[1], data_list[2], int(data_list[3]), int(data_list[4]))
                shoe_list.append(new_shoe)
            except Exception as error_string:
                print(f"Error found in inventory.txt: \033[3m{error_string}\033[0m in line \033[3m{line}\033[0m")

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    print("\nAdding new product to inventory.\n")
    while True:
        new_code = input("Please enter the product code or type 0 to cancel: SKU").strip().strip("SKU")
        if new_code == "0":
            return 0
        elif new_code.isdigit():
            new_code = "SKU" + new_code
            if code_match(new_code, shoe_list) == -1:
                break
            else:
                print(f"Error: Another item with that code was found. Try again.")
                continue
        print("Invalid input. Please be sure to enter numbers only.")
    while True:
        new_name = input("Please enter the product name: ").strip()
        if new_name.replace(" ", "").replace(".", "").isalnum():
            break
        print("Invalid input. Please be sure to enter letters and numbers.")
    while True:
        new_country = input("Please enter the product country: ").strip()
        if new_country.replace(" ", "").isalpha():
            break
        print("Invalid input. Please be sure to enter letters only.")
    while True:
        new_cost = input("Please enter the product cost: ").strip()
        try:
            new_cost = int(new_cost)
            if new_cost <= 0:
                raise ValueError
            break
        except Exception:
            print("Invalid input. Please be sure to enter a positive number only.")
    while True:
        new_quantity = input("Please enter the product quantity: ").strip()
        try: 
            new_quantity = int(new_quantity)
            if new_quantity < 0:
                raise ValueError
            break
        except:
            print("Invalid input. Please be sure to enter a whole number only.")
    new_shoe = Shoe(new_country, new_code, new_name, new_cost, new_quantity)
    shoe_list.append(new_shoe)

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    print("\nPrinting all:")
    for shoe in shoe_list:
        print(shoe.__str__())

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    least_item_index = 0
    for current_index, shoe in enumerate(shoe_list):
        if shoe.get_quantity() < shoe_list[least_item_index].get_quantity():
            least_item_index = current_index
    restock_shoe = deepcopy(shoe_list[least_item_index])
    print(f"\nRestocking {restock_shoe.product}. Current quantity: {restock_shoe.quantity}")
    while True:
        order_quantity = input("Please enter the quantity you would like to order: ")
        try:
            order_quantity = int(order_quantity)
            break
        except Exception:
            print("Error - try again.")
    shoe_list[least_item_index].update_quantity(shoe_list[least_item_index].get_quantity() + order_quantity)
    restock_list_index = code_match(restock_shoe.code, order_list)
    if restock_list_index == -1:
        restock_shoe.update_quantity(order_quantity)
        order_list.append(restock_shoe)
    else:
        restock_shoe = order_list[restock_list_index]
        restock_shoe.update_quantity(restock_shoe.get_quantity() + order_quantity)
    print(f'''\nAdded {order_quantity} x {restock_shoe.product} ({restock_shoe.code}) to order list.
Stock quantity updated in inventory to {shoe_list[least_item_index].quantity}.''')

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    while True:
        user_code = input("\nEnter the code of the item or type Cancel: SKU").strip().strip("SKU")
        if user_code.lower() == "cancel":
            break
        if not user_code.isdigit():
            print("Invalid input. Please be sure you enter only numbers.")
            continue
        user_code = "SKU" + user_code
        shoe_list_index = code_match(user_code, shoe_list)
        if shoe_list_index == -1:
            print("Item not found.")
            continue
        print(shoe_list[shoe_list_index].__str__())
        break
    while True:
        menu_option = input("\nWould you like to edit this item? Enter yes or no: ").strip().lower()
        if menu_option == "no":
            break
        elif menu_option == "yes":
            shoe_list[shoe_list_index].edit_quantity()
            shoe_list[shoe_list_index].edit_cost()
            break
        else:
            print("Invalid input.")
                
def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    total_inventory = 0
    table_list = [["Item (SKU)", "Quantity", "Value"]]
    for shoe in shoe_list:
        table_list.append([f"{shoe.product} ({shoe.code})", f"x{shoe.quantity}", 
                           f"R{shoe.get_cost() * shoe.get_quantity()}"])
        total_inventory += (shoe.get_cost() * shoe.get_quantity())
    total_inventory = f"R{total_inventory}"
    table_list.append([f"\033[1mTotal Inventory\033[0m", "", f"\033[1m{total_inventory}\033[0m"])
    print("\nPrinting current inventory value for each item: ")
    print(tabulate(table_list, colalign=("left", "right", "right")))

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    most_index = 0
    for current_index, shoe in enumerate(shoe_list):
        if shoe.get_quantity() > shoe_list[most_index].get_quantity():
            if not shoe in sale_list:
                most_index = current_index
    most_item = shoe_list[most_index]
    print(f"\nThere are {most_item.get_quantity()} {most_item.product} in inventory.")
    print(f"{most_item.product} should be listed on sale.")
    sale_list.append(most_item)
    return most_item


#==================== Populate shoe_list from inventory.txt ==============
print("\n\n" + "=" * 75 + "\n\n\033[1mWelcome to Inventory Manager.\033[0m")
read_shoes_data()

#========================== Main Menu loop ======================================

while True:
    menu_choice = input("\n\n" + "* " * 25 + '''\nPlease choose one of the following options:\n
View - view all inventory
Search - search for a shoe by SKU
Add - add new item to inventory
Restock - restock the item with the least stock
Sale - mark the item with the most stock as on sale
Value - view the item and total inventory value
Exit - save changes and exit the program
\nType option here: ''').strip().lower()

    if menu_choice == "view":
        view_all()

    elif menu_choice == "search":
        search_shoe()

    elif menu_choice == "add":
        capture_shoes()

    elif menu_choice == "restock":
        re_stock()

    elif menu_choice == "sale":
        highest_qty()

    elif menu_choice == "value":
        value_per_item()

    elif menu_choice == "exit":
        break

    else:
        print("Invalid option.")


#======================= Save, print summary, end program ===========================
print("\n\033[1m" + "-" * 75 + "\nSession summary:\n\033[0m")

order_list_table = []
order_headers = ["Product (SKU)", "Quantity to order"]
[order_list_table.append([f"{shoe.product} ({shoe.code})", shoe.quantity]) for shoe in order_list]
if len(order_list_table) >= 1:
    print("\n\033[3mShoes and quantities that must be ordered:\033[0m")
    print(tabulate(order_list_table, order_headers, tablefmt="simple_outline"))
else: 
    print("\nOrder list is empty.")

if len(sale_list) > 0:
    print("\n\033[3mPrinting list of shoes that should be marked as sale items:\033[0m")
    [print(shoe.product) for shoe in sale_list]
else:
    print("\nSale list is empty.")

with open("inventory.txt", "w") as inventory_file:
    print("\nSaving your changes to storage.")
    inventory_file.write("Country,Code,Product,Cost,Quantity\n")
    [inventory_file.write(shoe.file_string()) for shoe in shoe_list]

print("\nGoodbye!\n" + "-" * 75)