from graphics import *
win = GraphWin("My Fractal", 1600, 1000)
win.setBackground(color="white")


from math import *

def find_point(p1, distance, angle):
   rad_angle = -1 * radians(angle)
   xcor = cos(rad_angle) * distance + p1.getX()
   ycor = sin(rad_angle) * distance + p1.getY()
   return Point(xcor, ycor)


from Queues import *
def fractal():
    q = Queue()
    q.enqueue([12, 250, 0, 400,500])
    my_poly = Polygon()

    while not q.empty():
       q0 = q.dequeue()
       d = q0[0]
       dist = q0[1]
       ang = q0[2]
       x1 = q0[3]
       y1 = q0[4]
       found_point1 = find_point(p1=Point(x1, y1), distance=dist, angle=ang)
       Line(Point(x1, y1), Point(found_point1.getX(), found_point1.getY())).draw(win)
       found_point2 = find_point(p1=Point(x1, y1), distance=dist, angle=ang+90)
       Line(Point(x1, y1), Point(found_point2.getX(), found_point2.getY())).draw(win)
       found_point3 = find_point(p1=Point(found_point2.getX(), found_point2.getY()), distance=dist, angle=ang+360)
       Line(Point(found_point2.getX(), found_point2.getY()), Point(found_point3.getX(), found_point3.getY())).draw(win)
       Line(Point(found_point1.getX(), found_point1.getY()), Point(found_point3.getX(), found_point3.getY())).draw(win)
       if d > 0:
           q.enqueue((d-1, dist*0.6, ang+290, found_point1.getX(), found_point1.getY()))
           q.enqueue((d - 1, dist*0.6, ang+110, found_point2.getX(), found_point2.getY()))
           q.enqueue((d - 1, dist * 0.6, ang +380, found_point3.getX(), found_point3.getY()))
    win.getMouse() # Pause to view result
    win.close()

fractal()


#no color yet- hopefully coming soon