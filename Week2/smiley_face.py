from graphics import *

win = GraphWin('Smile?',300,300)
point = Point(100,200)


circle = Circle(point,80)
circle.setOutline('black')
circle.setFill('yellow')
circle.draw(win)

second_point = Point(140,250)
line = Line(Point(90,250),second_point)
line.draw(win)

third_point = Point(90,170)
another_circle = Circle(third_point, 10)
another_circle.setOutline('black')
another_circle.setFill("black")
another_circle.draw(win)

fourth_point = Point(140,170)
eye2_circle = Circle(fourth_point, 10)
eye2_circle.setOutline('black')
eye2_circle.setFill("black")
eye2_circle.draw(win)

win.getMouse()
win.close()
close = input("Press any key to close window.")