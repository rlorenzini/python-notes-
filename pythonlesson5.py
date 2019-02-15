##OBJECTS AND CLASSES

#CLASS = BLUEPRINT
#CLASSES have hierarchies
#CAR would be the SUPERCLASS
#HONDA ACCORD would be the SUBCLASS
#make, model, color, year would be the PROPERTIES of the CLASS

#Car (Class)
#- color
#- make
#- model
#- year
#- price
#- wheels
#- doors
#Class can have functions
#methods:
#    ignition(on_off)
#    steer(degrees)
#    shift_gear(gear_number)



#Toyota Corolla is a Car
#green
#Toyota
#Corolla
#2015
#$13000.00
#4
#4

#Dog class. Dog blue print. def ___init___ MUST HAVE TWO _ to INITIALIZE
class Dog:
    def __init__(self,name): #in PYTHON first argument is ALWAYS self for functions; no pass required
        self.name = name #self represents OBJECT being used; name = PROPERTY
        print("Dog is initialized..")
#create OBJECT of the Dog CLASS
dog = Dog('Dog 1')
print(dog.name) #print(OBJECT.property)

another_dog = Dog("Another Dog")
print(another_dog.name)


class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        print("Car is initialized. Drive safely.")
    def start(self):
        print("Starting the car... Vroom, vroom.")
    def crashing(self):
        print("Learn to drive, you idiot!")

car = Car('Toyota', 'Corolla', '2015', 'Green')
print(car.make, car.model, car.year, car.color)
car.start()

car2 = Car('Honda', 'Accord', '1999', 'Yellow')
print(car2.make, car2.model, car2.year, car2.color)
car2.start()
user_input = ""
def oops():
    user_input = input("Did you crash? Y/N: ").lower()
    if user_input == "y":
        car2.crashing()
    else:
        print("Keep driving safely!")
oops()

class Task:
    def __init__(self, title, priority,date1,date2):
        self.title = title
        self.priority = priority
        self.isCompleted = False
        self.username = 'Richard'
        self.date_created = date1
        self.date_completed = date2
    def mark_as_completed(self):
        self.isCompleted = True
    def print_task(self):
        print(self.title + " - " + self.priority + " - " + self.date_created + " - " + self.date_completed)
task = Task('mow the lawn','high','10/24/1992','10/25/1992')
task.isCompleted = True

task.print_task()
