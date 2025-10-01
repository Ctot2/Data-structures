class Rectangle:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return "width of " + str(self.width) + " and a height of " + str(self.height)

new_rectangle = Rectangle(8, 5)
print(new_rectangle.get_area())
print("a rectangle with a " + str(new_rectangle))
