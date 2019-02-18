##classes, iterations
##REVIEW

class Dog:
    def __init__(self,name,age=1): #must have self, must init class
        self.name = name #self.parameter = init(parameter)
        self.age = age #age=1 unless self.age value is entered
        self.owner = "John" #owner defaults to John with no option to change
    def walk(self):
        print("Walking")
    def eat(self,food):
        print(f"Eating {food}.")
dane = Dog("Flurffy",7)
print(dane.name,dane.age,dane.owner)
dane.owner = "Robert" #will need to change owner like this since there is no owner parameter is class Dog
dane.walk() #runs function walk() as is
dane.eat("tacos") #inserts tacos into food parameter then runs eat()

class BankAccount:
    def __init__(self,driver_license,initial_deposit,type_of_account):
        self.driver_license = driver_license
        self.balance = initial_deposit
        self.type_of_account = type_of_account
    def deposit(self,amount):
        self.balance += amount


bank_account = BankAccount("GA055569224", 100.00, "checking")
print(bank_account.balance)
bank_account.deposit(50.00)
print(bank_account.balance)

#################################################################
name = "John" #define name as john
another_name = name #create a new value for name
another_name = "Mary"

print(name)
print(another_name)

numbers = [1,2,3,4,5] #making a copy of numbers and allowing us to modify it without changing the original copy
another_numbers = numbers
another_numbers.append(99)
print(numbers)
##This is called a REFERENCE TYPE   ##########
#REFERENCE TYPES are stored in the memory; called HEAP
#The HEAP points the stored REFERENCE to a particular value (the array, not the variable)
#When you make a copy and assign it, this is called a VALUE TYPE
##REFERENCE TYPE == original, VALUE TYPES == modified from copy of original
##REFERENCE TYPES == ARRAYS, CLASSES
#If you change the REFERENCE TYPE it changes the value for all subsequent calls

class Cat:
    def __init__(self,name):
        self.name = name
    def __repr__(self): #changing how default outputs are represented (disable and see how print(cats) displays)
        return self.name

cat1 = Cat("Cat 1")

cat2 = cat1
print(cat1.name)
print(cat2.name)

cat2.name = "Cat 99"
print(cat2.name)
print(cat1.name)

cat3 = Cat("Cat 3")

cats = [cat1,cat3]
print(cats) #reference line 56 and 57

cat1.name = "Another Cat"

for cat in cats:
    print(cat.name)
###   NHERITENCE   ##################
class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
        self.speed = 100
        self.color = "Yellow"
    def drive(self):
        print("\nDrive.\n")
    def brake(self):
        print("\nBrake.\n")
    def fill_up_gas(self):
        print("\nFilling up now.\n")
class ElectricCar(Car): #ElectricCar Class INHERITS from Car class
    def __init__(self,make,model): #initializing is a good idea since superclass tends to have more info
        #super means parent class (Car is SUPER to ElectricCar)
        super().__init__(make,model)
#car already defines what make and model are, and electriccar inherits them
#drive and brake are inherited, so you do not need to type them again
#super will call self.color, so when ElectricCar.color is called it uses the value of Car.color
    def fill_up_gas(self):
        print("\nYour electric car needs gas???\n") ##override values of fill_up_gas() with new value
#using SUPER is important to save time
electric_car = ElectricCar("Tesla","Model 3")
print(electric_car.make, electric_car.model, electric_car.color)
#INHERITENCE saves a ton of time by avoiding typing or copying code over and over
electric_car.drive()
electric_car.fill_up_gas()  #will not run Car.fill_up_gas since ElectricCar overrides it


##Another example
class Animal:
    def __init__(self,name):
        self.name = name
        print("initialized")
    def eat(self):
        print("eating")
    def sleep(self):
        print("sleeping...")
##NOTE: if a function doesnt pull, user super.function or copy function
## calling functions isnt always the best optiong
class Cat(Animal):
    def __init__(self):
        super().__init__(name)
        self.speed = 65
class Cheetah(Cat):
    def __init__(self):
        super().__init__(name)
## you can create an endless heirarchy of SUPER and SUB CLASSES
##Cheetah is a cat; a cat is an animal
#Cheetah can have properties which the superclasses do not have
#Transportation == SUPER
#LandVehicles, WaterVehicles, AirVehicles, SpaceVehicles == SUB of SUPER
#Cars, ElectricCars, Motorcycles == SUB of LandVehicles
#Trucks, SUVs, Suburbans, Sedans == SUB of Cars

class Address:
    def __init__(self,street,city,state,zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
    def __repr__(self):
        return self.street
    def __repr__(self):
        return self.city
    def __repr__(self):
        return self.state
    def __repr__(self):
        return self.zip

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = []
    def __repr__(self):
        return self.first_name
    def __repr__(self):
        return self.last_name

user = User("John","Doe")
address1 = Address("Street","City","Texas","77380")

user.addresses = address1
print(user.addresses.street, user.addresses.city, user.addresses.state, user.addresses.zip)
print(user, "THIS IS WHAT IM LOOKING FOR")


print(user.addresses)

##NOT FULLY FUNCTION; cannot append array and print it 
