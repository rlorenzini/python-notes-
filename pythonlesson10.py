from graphics import *

###Time to make stuff look purrrrrrrdy in PYTHON


#define a window
win = GraphWin('Window 1', 600, 600)


#circle needs two POINT inputs (x axis, y axis)
#0,0
#1,0   1,10    1,20
#20,0  20,10   20,20
point = Point(300,300)
circle = Circle(point,50)
#draw circle in win
circle.draw(win)
circle.setOutline('yellow')
circle.setFill('blue')
#draw a line from out previous point object to a new Point(value); can interchange objects and Point() without issue
line = Line(point,(Point(450,0)))
line.draw(win)
#ask for user mouse input
win.getMouse()
#close the window
win.close()
#keeps the window from closing automatically
input("Press any key to exit.\n::")
