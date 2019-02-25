filename = open("pool_table_info.txt", "w")
from datetime import datetime
#import json
user_input = ""
tables = []


def menu():
    print("Press 1 to view all the tables:")
    print("Press 2 to check out a table:")
    print("Press 3 to check in:")
    print("Press q to quit")


class PoolTable:
    def __init__(self,table_no):
        self.table_no = table_no
        self.avaiable = True 
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.total_time = 0
    
    def check_in(self):
       self.avaiable = False
       self.start_time = datetime.now()
       self.end_time = "null"
       self.total_time = "null"
       print(f'{self.table_no} | {self.start_time}') 

    def check_out(self): 
        self.avaiable = True
        self.end_time = datetime.now()
        self.total_time = self.end_time - self.start_time
        print(f"{self.table_no}: /n {self.start_time} /n {self.end_time} /n {self.total_time}")


        with open("pool_table_info.txt","a") as user_info:
            user_info.write(f"{self.table_no}: {self.start_time} \n {self.end_time} \n {self.total_time} \n") #tables is the array and im putting my array of tables into user_info my json file


def view_tables():
    for table in tables:
        print(f"Table {table.table_no}") 
        if  table.avaiable == False:
            print('This table is occupied.')
        else:
            print('UNOCCUPIED')


for index in range(1,13):
    table = PoolTable(index)
    tables.append(table)

while user_input!= "q":
    menu()
    user_input = input("Enter your choice: ") 

    if user_input  == "1":
            view_tables()
    elif user_input == "2":
        view_tables()
        try:
         user_input = int(input("What table number are you checking out?"))
        except ValueError:
         print("ERROR: try again must input a number.")
        table_number = tables[user_input-1]#set table to that specific table
        table_number.check_in()
        view_tables()
    elif user_input == "3":
        try:
         user_input = int(input("What table number are you checking in?"))
        except ValueError:
         print("ERROR: try again must input a number.")
        table_number = tables[user_input-1]#set table to that specific table
        table_number.check_out()
        view_tables()
    else:
        if user_input != "q":
         print("Something went wrong try again.")
           
