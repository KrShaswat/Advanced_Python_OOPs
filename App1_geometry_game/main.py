from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        if rect.point1.x < self.x < rect.point2.x \
                and rect.point1.y < self.y < rect.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return int(self.point2.x - self.point1.x) * \
               int(self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        height = int(self.point2.x - self.point1.x)
        width = int(self.point2.y - self.point1.y)

        # goto the first point
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()

        # start the rect draw

        canvas.forward(width)
        canvas.left(90)
        canvas.forward(height)
        canvas.left(90)
        canvas.forward(width)

        canvas.left(90)
        canvas.forward(height)

class GuiPoint(Point):
    def draw(self, canvas, size=5, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


rectangle = GuiRectangle(
    Point(randint(0, 400), randint(0, 400)),
    Point(randint(10, 400), randint(10, 400)))

print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ",user_point.falls_in_rectangle(rectangle))
print("Your area is off by: ", rectangle.area() - user_area)
myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()