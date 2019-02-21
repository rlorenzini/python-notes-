from graphics import *

###Time to make stuff look purrrrrrrdy in PYTHON


#define a window
win = GraphWin('Window 1', 600, 600)


#circle needs two POINT inputs (x axis, y axis)
#0,0
#1,0   1,10    1,20
#20,0  20,10   20,20
point = Point(300,300)
circle = Circle(point,300)
#draw circle in win
circle.draw(win)
circle.setOutline('black')
circle.setFill('yellow')


left = Point(200,200)
right = Point(400,200)
lefteye = Circle(left,60)
righteye = Circle(right,60)
lefteye.setFill('white')
righteye.setFill('white')

lefteye.draw(win)
righteye.draw(win)

start = Point(200,400)
end = Point(400,400)
line = Line(start,end)
line.draw(win)

irisleft = Circle(left,40)
irisleft.setFill('blue')
irisleft.draw(win)
irisright = Circle(right,40)
irisright.setFill('blue')
irisright.draw(win)

pupilleft = Circle(left,30)


pupilleft.setFill('black')
pupilleft.draw(win)
pupilright = Circle(right,30)
pupilright.setFill('black')
pupilright.draw(win)

smile = Oval(Point(200,400), Point(400,300))
smile.setOutline('black')
smile.draw(win)

#draw a line from out previous point object to a new Point(value); can interchange objects and Point() without issue
# line = Line(point,(Point(450,0)))
# line.draw(win)
#ask for user mouse input
win.getMouse()
#close the window
win.close()
#keeps the window from closing automatically
# input("Press any key to exit.\n::")
