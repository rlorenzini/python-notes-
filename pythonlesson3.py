##DICTIONARIES AND CODE MODULES


## REVIEW:


#basic input
def is_palindrome(word):
    rev = ""
    #defining rev to equal nothing atm
    for index in range (len(word)-1,-1,-1):
        #range (len(XXX))-1 says start from end and move to the start
        rev = rev + word[index]
    #rev equals word in reverse
    if rev.lower() == word:
        print("PALINDOME")
    #adding .lower() to remove case sensitivity
    #if reverse == word then print true
    else:
        print("NOPE")
word = input("Enter Word: ").lower()
is_palindrome(word)
#defining word is input and place input in function

def is_palindrome(word):
    result = False
    #defining result as false instead of else: result = false
    rev = ""
    for index in range (len(word)-1, -1, -1):
        rev = rev + word[index]
    if rev.lower() == word:
        result = True
    #if palindrome then result now = true
    return result
    #return result so is_paindrome(word) = true

word = input("Enter Word: ").lower()
#getting user input for above function
result = is_palindrome(word)
#result = result of function
print(result)
#prints true or false based on what function returns

if is_palindrome(word):
    print("PALINDROME")
else:
    print("NOPE")
#must have a return in function for if else here to work
#if true then print palindrome
#else (if false) print nope


###MODULES  - packaging code without copy pasting
#python has a package for math that allows you to do algorithms without typing it out
#ex: instead of creating a function to do a factorial, call upon the python math package
import math
#will now be able to use all of python's math package

result = math.factorial(5)
print(result) #5! = 120
#similar to how you create a function and then reference it later, such as is_palindrome above
#using a module tells your current project of previously defined functions that exist
#you can now use the functions without having to add the code to your project

#but how do we add our functions into a module and call upon it?
#reference testmodule.py
import testmodule
print(testmodule.add(2,3))

#create a file for the functions
#import the test file (no need for .py)
#specify the module and function from module
#<file>.<function>
#math and testmodule both have add functions and will conflict otherwise



#what if module is in another directory?
#import sys
#sys.path.append("")


#giving alias to module is import <module> as <alias>

import testmodule as m
print(m.subtract(5,3))

#can you import only one function? YES
#from <module> import <function>
from testmodule import add
print(add(9,7))
#now you can use the function without needing to reference the module each time

from testmodule import *
#now ALL functions are imported and you can use without module.function

print(subtract(9,7))

#when importing multiple modules it can be wise to use module.function
#so others reading your code know where the function comes from
#and can look up exactly what it does when needing to troubleshoot


#WHY USE MODULES???
#would you rather go through 10k lines of code
#or know function add is failing, find function add is from module X
#and go to module X to troubleshoot 10 lines?
#modules help with future troubleshooting issues and saving time 
