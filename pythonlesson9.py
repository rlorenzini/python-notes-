# FILES

try:
    test_object = open('testingfilefunctions.txt') #by default, without any arguments after the ' ', open() starts reading the file
except FileNotFoundError:
    print("File 'testingfilefunctions.txt' does not exist. Create the file before trying to open it.")
#open() arguments:
#'w' = write; 'r' = read (default); 'a' = appending

try:
    file_object = open('names.txt', 'w') #'w' creates a file, and if the file already exists it overwrites the file
    #by default, creates the file in your current working directory
    file_object.write("Hello World!\n") #\n creates a new line break
    file_object.write("Line 2")
    file_object = close() #always call close() to prevent others from accessing the file and from wasting resources
except:
    print("Something went wrong.")
#good practice is to close a file after it is immediately used and open it the next time you need it
#avoid having multiple files open if you can


try:
    with open('names.txt', 'w') as file_object: #dont forget your arguments ('w')
        file_object.write("Using With Operator")
        file_object.write("New print() line does not create a break. \nMust use line break.")
except:
    print("With Operator did not work properly.")
with open('names.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
#will print line by line from the file
#without rstrip() the lines have a gap between them; rstrip() removes the space
with open('names.txt') as file_object:
    lines = file_object.readlines()
print(lines)
#appends the file lines into an array; now you can manipulate individual lines and call on them
#NOTE:: \n counts as a line break; will not break apart two separate .write()s without \n

#'w' recreates the file and writes over it; not good for building any list or extending a file's data/text
#'a' appends, allowing you to add without removing previous data
with open('names.txt', 'a') as file_object:
    file_object.write('\nAnother new line, which starts with a line break \ n ')
#adds the new line without deleting the old lines, like 'w' had done previously
file_object = close()
