import unittest
from pythonreview8 import *

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        print("setUp")
    def test_should_create_a_file(self):
        file_object = open('somefile.txt','w')
        file_object.write('hello world')
        file_object.close()
    #bad test: should delete a file after file is finished being used
    #no test_file should leave ANY trace behind
    def tearDown(self):
        #tearDown deletes files and cleans up resources after every test is executed
        print("tearDown requires setUp to exist")
    #setUp > Test > tearDown > ...
    def test_should_be_able_to_create_shopping_list(self):
        shopping_list = ShoppingList('HEB')
        self.assertIsNotNone(shopping_list)
    def test_add_item_to_shopping_list(self):
        shopping_list = ShoppingList('Kroger')
        grocery_item = GroceryItem('Soda')
        shopping_list.add_grocery_item(grocery_item)
        self.assertEqual(1, len(shopping_list.grocery_items))


unittest.main()
