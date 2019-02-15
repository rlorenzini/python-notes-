##REVIEW
user = {"first_name": "Richard", "last_name": "Lorenzini"}
#print(user)

#user["first_name"] = "AnneMarie"
#print(user)

address = {"street": "Canal Street",
    "city": "Houston",
    "state": "Texas"}
#print(address)

user["address"] = address
#print(user)

geo = {"Longitude": "-37", "Latitude": "81"}

address["geo"] = geo
#print(user)
#always organize dictionaries into hierarchies for future data display
#easier to display just address[] than to remove user[] and geo[]
airports = {"IAH": "Intercontinental Airport"}

airports["SJO"] = "San Jose Airport"
#dict["key"] = "value"
#print(airports)

student = {"name": "John", "age": 24, "is_graduated": True}
#print(student)

task_list = []
user_input = ""

def show_menu():
    print("Press 1 to add new task: ")
    print("Press 2 to delete task:")
    print("Press 3 to view all tasks:")
    print("Press q to quit: ")
show_menu()

def add_task(): #add task to list
        task = input("Enter Task Name:")
        priority = input("Enter Task Priority: ")
        task = {"task": task, "priority": priority}
        task_list.append(task)
        print(task)

def show_list(): #print full task list
    for index in range(0,len(task_list)):
        task = task_list[index]
        print(f"{index + 1} - {task['task']} - {task['priority']}")

def delete_task(): #delete task number o
    show_list()
    task_id = int(input("Enter Task Number To Delete: "))
    del task_list[task_id -1]

while user_input != "q": #user selection
    user_input = input("Enter your choice: ").lower()
    if user_input == "1":
        add_task()
    elif user_input == "2":
        delete_task()
    elif user_input == "3":
        show_list()



















#
