class ShoppingList:
    def __init__(self,name):
        self.name = name
        self.grocery_items = []
    def add_grocery_item(self,grocery_item):
        self.grocery_items.append(grocery_item)

class GroceryItem:
    def __init__(self,name):
        pass
