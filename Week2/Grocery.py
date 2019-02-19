user_input = ""
stores = []




def menu():
    print("Press 1 to add a store:")
    print("Press 2 to add item to store list:")
    print("Press 3 view all shopping lists:")
    print("Press q to quit")


 
class Store: 
    def __init__(self,store_name):
        self.store_name = store_name
        self.grocery_items = []
        

class StoreItem:
    def __init__(self,item,quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price
        


    # def subtotal(self):



        
def add_shopping_list():
    name = input("Store name:")
    shopping_list = Store(name)
    stores.append(shopping_list)

def view_all_stores():
    
    for index in range(0,len(stores)):
        shopping_list = stores[index]
        print(f"{index+1} - {shopping_list.store_name}")
        for grocery_item in shopping_list.grocery_items:
            print(f"{grocery_item.item} - {grocery_item.quantity} - {grocery_item.price}")

def add_item():
    view_all_stores()
    shopping_list_number = int(input("Enter shopping list number to add the grocery item:"))
    shopping_list = stores[shopping_list_number -1]
    item = input("Enter the item:")
    quantity = float(input("Enter quantity:"))
    price = float(input("Enter price of item:"))
    grocery_items = StoreItem(item,quantity,price)

    shopping_list.grocery_items.append(grocery_items)
    
def store_item_total():
    view_all_stores()
    for index in range(0,len(stores)):
        print(index)

while user_input != "q":
        menu()
        user_input = input("Enter your choice: ")
        if user_input  == "1":
            add_shopping_list()
        elif user_input == "2":
            add_item()
        elif user_input == "3":
            view_all_stores()
            store_item_total()


    
    
        
    
    





