tasks = []
user_input = ""



  

def menu():
        print("Press 1 to add to your list:")
        print("Press 2 to delete tasks:")
        print("Press 3 to look at your list:")
        print("Press q to quit:")
 



def add_task():
    task_name = input("Enter title of task:") 
    task_priority = input("Enter priority of task:")
    
    your_task = {"title": task_name, "priority": task_priority}
        
    tasks.append(your_task)
    


def view_all():
    for index in range(0,len(tasks)):
        j = tasks[index]
        print(f"{index + 1} - { j['title']} - {j['priority']}")
    

      
  

def delete():
        view_all()
        user_input = int(input("Enter the task number you have completed:"))
        del tasks[user_input -1]
        view_all()
        
        
    


while user_input != "q":
    menu()
    user_input = input("Enter your choice: ")

    if user_input  == "1":
        add_task()
    elif user_input == "2":
         delete()
    elif user_input == "3":
        view_all()







