from lib import User, Painter
import turtle, random

usr = User()
num_sides, size, orientation, location, color, border_size = usr.drawing_prep()

painter = Painter(num_sides, size, orientation, location, color, border_size)
painter.setup(0, "black", 0, 255)

painter.draw_polygon()

reduction_ratio = 0.618

# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio

# draw the second polygon embedded inside the original
painter.size = size
painter.draw_polygon()

turtle.done()