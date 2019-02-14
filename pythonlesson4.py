##DICTIONARIES - reference dicttest.py

#works like a dictionary or phonebook
#if looking for John you skip forward to J
#you don't got page by page from AA - JO

#dictionary always has key and value; in python use {} for dictionary and [] to call key
#{key:value,key:value,key:value}
airports = {"IAH":"Intercontinental Airport"}

#ex:   student = {"studentid:23859402384"}


print(airports["IAH"])
#must use [] to call key and value in PYTHON
#by default it is case sensitive
#will print error message if it cannot find exact key or value
user1 = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 30,
    "street": "1200 Road Street"
}
#another way to create a dictionary for a specific variable (such as user info)
print(user1)

car = {
    "make": "Toyota",
    "model": "Corolla",
    "year": 2015
}
#dictionary is meant to hold multiple values

alphabets = {
    "A": "ALPHA",
    "B": "BRAVO",
    "C": "CHARLIE"
}
alphabets["D"] = "DELTA"
#create a new key D for dictionary alphabets and assign it value DELTA
print(alphabets)
#prints A B C and D values

#dictionaries get messy fast
#keep your keys and values organized
#keys need to be the broad value (make, model, title) and values are specific
#values = Toyota, Corolla, MacBook

#asking user for data list and storing it in dictionary

tasks = []
#task is an empty array
def view_all_tasks():
    for task in tasks:
        print(task)


def show_menu():
    print("Press 1 to add a new task: ")
    print("Press q to quit: ")
    #showing user a basic menu
def add_new_task():
    task_name = input("Enter name of task: ")
    task_priority = input("Enter priority: ")
    #create a dictionary
    task = {"title": task_name, "priority": task_priority}
    #now input values are stored into the dictionary <task>
    tasks.append(task)
    #adding dictionary <tasks> to array <task>
#showing a menu for users
user_input = ""
#user_input has no value as of now
while user_input != "q":
    show_menu()
    user_input = input("Enter your choice: ")
    #first input request for user; q or 1
    if user_input == "1":
            add_new_task()
            #if 1, call on addnewtask function above
    else:
        view_all_tasks()


#to go through each value of the dictionary
#for (key,value) in <dictionary>.items():
    #print(key)
    #print(value)


#to only print keys or values
#for key in <dictionary>.keys():
    #print(key)
    #print(<dictionary[key])

#second print will print value of key entered


#removing items from dictionary
#del <dictionary>[key]


#
