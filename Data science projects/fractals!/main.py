from graphics import *
win = GraphWin("My Fractal", 1000, 800)
win.setBackground(color = "white")

# Close window when done


from math import *

def find_point(p1, distance, angle):
   rad_angle = -1 * radians(angle)
   xcor = cos(rad_angle) * distance + p1.getX()
   ycor = sin(rad_angle) * distance + p1.getY()
   return Point(xcor, ycor)

def fractal_spiral(d, dist, ang, x1, y1):
    if d == 0:
        return
    else:
        found_point = find_point(p1=Point(x1, y1), distance=dist, angle=ang)
        Line(Point(x1, y1), Point(found_point.getX(), found_point.getY())).draw(win)
        fractal_spiral(d-1, dist*0.75, ang-90, found_point.getX(), found_point.getY())
        fractal_spiral(d - 1, dist/1.5, ang +20, found_point.getX(), found_point.getY())


fractal_spiral(15, 200, 90, 500,800)
win.getMouse() # Pause to view result
win.close()