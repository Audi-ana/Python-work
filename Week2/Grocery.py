user_input = ""
stores = []

def menu():
    print("Press 1 to add a store:")
    print("Press 2 to add item to store list:")
    print("Press 3 view all stores:")
    print("Press q to quit")


 
class Store: 
    def __init__(self,store_name):
        self.store_name = store_name
        self.items = []


def add_store():
    store_name = input("Store name:")
    store = Store(store_name)
    stores.append(store)
    view_all_stores()

def view_all_stores():
    for store in stores:
        stores.index(store)
        print(f'{stores.index(store)+1} - {store.store_name}')

class ShoppingList:
    def __init__(self,item,quantity):
        self.item = item
        self.quantity = quantity


def add_item():
    x = ""
    x = print(f'New item:{item},{quantity}')
    Store.item.append(x)

    
    



    
   
    
while user_input != "q":
        menu()
        user_input = input("Enter your choice: ")
        if user_input  == "1":
            add_store()
        elif user_input == "2":
            add_item()
        elif user_input == "3":
            view_all_stores()
            
menu()



    
    
        
    
    





