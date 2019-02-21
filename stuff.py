allnames = []
user_input = ""

def askname():
    first = input("What is your first name? \n:")
    last = input("What is your last name? \n::")
    names = first,last
    allnames.append(names)
    print(names)
    print(allnames)

while user_input != 'q':
    user_input = input("1 or q. \n::")
    if user_input == '1':
        askname()
    if user_input == 'q':
        for x in allnames:
            print(x)
        exit()
