user_input = ""

shopping_lists = []


class ShoppingList:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        grocery_item = []
class GroceryList:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def show_menu():
    print("Enter 1 to add shopping list. ")
    print("Entetr 2 to add grocery item. ")
    print("Enter 3 to view shopping lists. ")
    print("Enter q to quit. ")
show_menu()
def add_shopping_list():
    name = input("Enter name of shopping list. ")
    address = input("Enter address of shopping list. ")
    store = ShoppingList(name, address)
    shopping_lists.append(store)
    show_menu()
def add_grocery_item():
    view_shopping_lists()
    number = input("Enter shopping list number to add grocery item to. ")
    grocery_list = shopping_lists[number - 1]
    name = input("Enter item. ")
    price = float(input("Enter price. "))
    quantity = int(input("Enter quantity. "))
    grocery = GroceryList(name, price, quantity)

    shopping_lists.grocery_item.append(grocery)

def view_shopping_lists():
    for index in range(0, len(shopping_lists)):
        stores = shopping_lists[index]
        print(f'{index+1} - {shopping_list.name}')
    for grocery in shopping_lists.grocery_item:
        print(f'{grocery.name} - {grocery.price} - {grocery.quantity}')
while user_input != 'q':
    user_input = input("Enter your choice. ").lower()
    if user_input == '1':
        add_shopping_list()
    elif user_input == '2':
        add_grocery_item()
    elif user_input == '3':
        view_shopping_lists()
