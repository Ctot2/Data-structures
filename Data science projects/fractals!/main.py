from graphics import *
win = GraphWin("My Fractal", 1000, 800)
win.setBackground(color="white")


from math import *

def find_point(p1, distance, angle):
   rad_angle = -1 * radians(angle)
   xcor = cos(rad_angle) * distance + p1.getX()
   ycor = sin(rad_angle) * distance + p1.getY()
   return Point(xcor, ycor)


def version1(d, dist, ang, x1, y1):
    if d == 0:
        return
    else:

        found_point = find_point(p1=Point(x1, y1), distance=dist, angle=ang)
        Line(Point(x1, y1), Point(found_point.getX(), found_point.getY())).draw(win)
        version1(d - 1, dist * 0.65, ang - 90, found_point.getX(), found_point.getY())
        version1(d - 1, dist / 1.5, ang + 30, found_point.getX(), found_point.getY())





from Queues import *
def version2():
    q = Queue()
    q.enqueue([6, 100, 90, 500,700])

    while not q.empty():
       q0 = q.dequeue()
       d = q0[0]
       dist = q0[1]
       ang = q0[2]
       x1 = q0[3]
       y1 = q0[4]
       found_point = find_point(p1=Point(x1, y1), distance=dist, angle=ang)
       Line(Point(x1, y1), Point(found_point.getX(), found_point.getY())).draw(win)

       if d > 0:
           q.enqueue((d - 1, dist * 0.65, ang - 90, found_point.getX(), found_point.getY()))
           q.enqueue((d - 1, dist / 1.5, ang + 30, found_point.getX(), found_point.getY()))

choice = input("choose your version! ")
if choice == "a":
    version1(6, 100, 90, 500,700)
elif choice == "b":
    version2()

win.getMouse() # Pause to view result
win.close()

