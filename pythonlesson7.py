##EXCEPTIONS

# print(1/0) will give an error message since you cannot divide a number by 0

# try:  ##TRY must have an EXCEPT and EXCEPT must have a TRY
#     print(1/0)
# except:
#     print("Something went wrong.")
#try/except is now an error message. when 1 divided by 0 fails, the system prints "Something went wrong."
#PYTHON uses TRY/EXCEPT, javascript has another name for it
def test():
    print(1/1)
    no = int(input("Enter a number: "))
    print(1/no)
try:
    test()
#you have to break your code to create clean and effective try/except arguments
except ZeroDivisionError:
    print("You are dividing by zero. ")
except ValueError:
    print("Input only whole numbers.")
except:
    print("Something went wrong. ")
else:
    print("No error occurred. ")
## FINALLY is at the end of your script, function, project, etc
finally: #finally will always run; usually used to clean up resources
    print("Finally happens always. ") ##ELSE and FINALLY are optional. You can use both, one, or none.
#if you are opening a file and something goes wrong use FINALLY to close the file
#when a string or float is entered the user gets the assigned error message
#otherwise the user gets a bunch of coding errors
#adding multiple try/except in your code is better than one giant generic one
#if you do int(input()) the error message should refer to the user not inputting an integer
#when you run the code, the error message that appears is the error class
#except ERRORCLASS: codecodecode is how you add multiple except values associated to specific error possibilities
