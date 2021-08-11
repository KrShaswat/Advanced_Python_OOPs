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

        # Create the canvas
        self.data = np.zeros((self.height, self.width,  3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):

        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)