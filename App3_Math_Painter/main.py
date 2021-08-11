import numpy as np
from PIL import Image


class Canvas:
    """
    Makes a canvas using three inputs of width, height and colour (Black/white).
    This canvas will hold all the Geometric shapes. Use .make() method to make the canvas after
    instantiating the class.
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self, imagepath):
        data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        data[:] = self.color

        img = Image.fromarray(data, 'RGB')
        img.save(imagepath)


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



class Square:
    """
    Makes a square using top left corner point and side
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side

    def make(self, canvas):
        


# Canvas class check

canvas = Canvas(500, 1000, (255, 255, 255))
canvas.make('files/check.png')
