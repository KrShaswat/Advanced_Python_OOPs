class Reactangle:
    """
    Makes a rectangle using top left corner point location and 2 sides.
    """

    def __init__(self, x, y, width, height, color):
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        self.color = color

    def make(self, canvas):
        canvas.data[self.y:self.y+self.height, self.x:self.x+self.width] = self.color


class Square:
    """
    Makes a square using top left corner point and side
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def make(self, canvas):
        canvas.data[self.y:self.y+self.side, self.x:self.x+self.side ] = self.color