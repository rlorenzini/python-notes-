## REVIEW:
#input() to ask for info from user
#int() float() str() to specify expected input in python
#def string(a,b):
    #sum = a=#b
    #return = sum
#self-contained algorithm
#result = string(a,b)
#print(result)   do to show results of algorithm
#when adding interchangable strings from input values, you must use f'{}'
#print(f"{first_number} {operator} {second_number} = {result}")
#when using f"" you do not break up strings with ""
#print(f"{first_number} is larger than {second_number}")
#print(f"{first_number} + {second_number} = {result})



#CONDITIONS
#== is conditional; if x == y, THEN z happens
#== " " if any specified value; % results excluded
#if operator == "+":
#    print("Addition")
#    x = 10
#    print(x)
#    y = 10
#    print(y)
#as long as if condition is met, all if functions will be executed when applied
#else:
#    print("INVALID")
#if anything else happens than the if functions specify then execute else function
#without else, error message or no result will execute; if you remove else print will ALWAYS print
#elif: else, if; if if function is not true, elif is checked; if elif is not true, else is executed
#elif can go on forever; first is checked first, last is checked last
#if comes first, elif comes second, else comes last; MUST BE IN THIS ORDER
#if operator == "+":
#   print("Addition")
#elif operator == "-":
#   print(f"{first_number} - {second_number}")
#else:
#   print("INVALID")

#age = int(input("Enter Age: "))
#name = input("Enter Name: ")
#if age < 21:
#   print("You are unable to buy alcohol.")
#else:
#   print("Enjoy alcoholism!")
#if age < 21 and name == "John" and LivesInHouston == 1...... can keep going with conditions

#if age < 21 or name == "John":
#   print("WELCOME")

#if or statements only need one condition met to be executed

#LIST-LOOPS/ARRAYS

#loops are variables which can hold multiple values

#an array is like a book; you start at the front cover and go to the very end
#arrays typically have the same data values, such as names, numbers, etc
#arrays can hold any number of items and any variety of data values
#twitter feed, facebook feed, news feed, search results, etc are all arrays
#var = [array,list]

numbers = [0,1,2,3,4,5,6,7,8,9]
#the first item has a value of 0; item 4 is the fifth item in the array (4)
print(numbers[4])
#displays 4


#LOOPS

for index in range(0,10):
    print(index)
#the range ends one less than the final number
#displays 0-9 instead of 0-10
#loops are the bread and butter of ALL coding
#PRACTICE PRACTICE PRACTICE

for number in range(0,100):
    if number % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
#prints alternating EVEN/ODD, starting with 0=EVEN

for num in range(0,100,2):
    if number % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
#0,100,2 - start at 0, end at 100, only run every other result

for num1 in range(100,0,-1):
    print(num1)
#must tell the loop to work backwards; by default they only move forwards

print(f"Length of the array is {len(numbers)}")
#len() tells you the length of an array
for index in range(0,len(numbers)):
    print(numbers[index])
#using 0,len() allows the loop to ALWAYS print the full array
#this allows you to modify the array with extra or less data without changing the value of the loop
#0,10 will always print the first to tenth result
#0,len() will always print the frist to last result

for value in range(0,8):
    print(numbers[value])
#print the data from numbers[] from 0,8



names = ["John","Mary","Beth","Richard"]

for  index in range(0,len(names)):
    print(names[index])

print("ANOTHER FOR LOOP WITHOUT INDEX")

for name in names:
    print(name)

#produce same results; both are telling the loop to run until end of array

# adding items to the array

names.append("Robert")
#append = add new item to array (names being the array)
for name in names:
    print(name)
#applies RETROACTIVELY and NOT for anything above
#JERRY does not exist in this function

#names.insert(index,elem) is used to put item in specific spot
names.insert(0,"Jerry")

del names[1]
#removes item 1 from array (JOHN = 1 now since JERRY = 0 after .insert)
for name in names:
    print(name)
#JOHN will never be referred to in any further functions calling on NAMES


#WHILE LOOPS

#while X applies, keep looping the array

health = 100

#while condition:
#   body of the loop

while health >= 0:
    print("HEALTH IS GOOD!")
    health = -1

#loop will not end until health is 0
#loop will run indefinitely since health cannot decrease atm
#by adding health = -1 after print() the loop only runs once

user_input = ""
#!= - NOT EQUAL TO
while user_input != "q":
    user_input = input("Enter your choice or q to quit: ")

#loop will keep asking for input until user enters q
print("Thanks for playing the game!")
#Once user enters q print() executes
#print() can be inside end of loop or after loop 
