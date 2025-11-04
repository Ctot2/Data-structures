from graphics import *
win = GraphWin("My Fractal", 1000, 800)

# Close window when done


from math import *

def find_point(p1, distance, angle):
   rad_angle = -1 * radians(angle)
   xcor = cos(rad_angle) * distance + p1.getX()
   ycor = sin(rad_angle) * distance + p1.getY()
   return Point(xcor, ycor)

def fractal_spiral(d, dist, x1, y1, x2, y2):
    if d == 0:
        return
    else:
        Line(Point(x1, y1), Point(x2, y2)).draw(win)
        found_point = find_point(p1=Point(x2, y2), distance=dist, angle=2)
        x3 = found_point.getX()
        y3 = found_point.getY()
        fractal_spiral(d-1, dist/2, x2, y2, x3, y3)


fractal_spiral(7, 100, 500, 800, 500, 700)
win.getMouse() # Pause to view result
win.close()