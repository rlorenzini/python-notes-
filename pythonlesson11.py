### STACK DATA STRUCTURES

#think of a stack of dishes; you have to move the top to get to the next one
#the last one you put on the stack is the first one to come off

#its standard to call your insert function push() when using stack
#push(1), push(2), push(dog), push(potato)
#potato, dog, 2, 1 with potato on top and 1 on bottom
#pop() is pulling the top item off and using it
#pop() == potato
#pop() == dog since potato has previously been removed
#pop() == 2, pop() ==1, pop() == no value to pop (try: pop(): except: return xyz)


#understanding the data structure and the functions of a STACK is important
#STACK may or may not be something you ever use

### QUEUE DATA STRUCTURES

#first in, first out (think lines of people at the grocery store checkout)
#enqueue() and dequeue() are the same as push() and pop()
#enqueue(1), enqueue(23), dequeue() == 1, dequeue() == 23
import random
array1 = []

class Stack:
    def __init__(self, value):
        self.value = value
    def push(self, value):
         array1.append(value)
    def pop(self):
        array1.pop()
x = 1
test1 = Stack(x)
print(array1)
test1.push(x)
print(array1)
test1.push(7)
test1.push(8)
test1.pop()
print(array1)


from collections import deque
queue = deque(["eric", "john", "michael"])
queue.append("terry")
queue.append("graham")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)


### BUBBLE SORT

#when data is entered in any order you can pull the data out in a specific order
#most common example is random numbers put into an array and pulled out from smallest to largest
#any SORT BY option could be using BUBBLE SORTING (price, size, color, time, distance)
arr = [14,456,34,213456,65,4444,3,567,65,23]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubbleSort(arr)
for i in range(len(arr)):
    print("%d" %arr[i])
