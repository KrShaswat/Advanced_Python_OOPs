from canvas import Canvas
from shapes import Reactangle, Square

# CLI
canvas_width = int(input("Width of Canvas (Pixels): "))
canvas_height = int(input("Height of Canvas (Pixels): "))
print("Color of the Canvas in RGB format (e.g white = (255,255,255): ")
color_R = int(input("R: "))
color_G = int(input("G: "))
color_B = int(input("B: "))
canvas_color = (color_R, color_G, color_B)

canvas_filepath = input("Enter the file name for the image: ")

canvas = Canvas(canvas_width, canvas_height, canvas_color)


end = True
while end:
    shape = input("What do you want to draw? (rectangle or square) Enter 'quit' to exit: ")
    if shape.lower() == 'rectangle':
        point_x = int(input("Enter the top left corner point's x co-ordinate: "))
        point_y = int(input("Enter the top left corner point's y co-ordinate: "))

        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height if the rectangle: "))

        print("Color of the Rectangle in RGB format (e.g white = (255,255,255): ")
        color_R = int(input("R: "))
        color_G = int(input("G: "))
        color_B = int(input("B: "))
        color = (color_R, color_G, color_B)

        rectangle = Reactangle(point_x, point_y, width, height, color)
        rectangle.make(canvas)
    elif shape.lower() == 'square':
        point_x = int(input("Enter the top left corner point's x co-ordinate: "))
        point_y = int(input("Enter the top left corner point's y co-ordinate: "))

        side = int(input("Enter the side if the square: "))

        print("Color of the Square in RGB format (e.g white = (255,255,255): ")
        color_R = int(input("R: "))
        color_G = int(input("G: "))
        color_B = int(input("B: "))
        color = (color_R, color_G, color_B)

        square = Square(point_x, point_y, side, color)
        square.make(canvas)
    elif shape.lower() == 'quit':
        break
    else:
        print("Invalid input try again")
        continue
# Canvas class check
canvas.make(f"printed/{canvas_filepath}.png")


