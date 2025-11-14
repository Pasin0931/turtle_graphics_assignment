from lib import Painter, Brush
import turtle, random

painter = Painter()
num_sides, size, orientation, location, color, border_size = painter.drawing_prep()

brush = Brush(num_sides, size, orientation, location, color, border_size)
brush.setup(0, "black", 0, 255)

# brush.draw_inside()
# brush.draw()

# for i in range(random.randint(25, 35)):
#     draw

turtle.done()