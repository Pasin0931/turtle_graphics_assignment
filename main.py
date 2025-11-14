from lib import Painter, Brush
import turtle, random

painter = Painter()
num_ch = painter.painter_choice()

num_sides, size, orientation, location, color, border_size = painter.drawing_prep()

brush = Brush(num_sides, size, orientation, location, color, border_size)
brush.setup(0, "black", 0, 255)

# brush.draw_inside()
# brush.draw()

def gennerate_canvas():
    for i in range(random.randint(25, 35)):
        brush.draw()
        s, o, l, c, b = painter.gennerate_solcb()
        brush.size = s
        brush.orientation = o
        brush.location = l
        brush.color = c
        brush.border_size = b

print("Gennerating Canvas . . .")

if num_ch == 1:
    brush.num_sides = 3
    gennerate_canvas()
    
elif num_ch == 2:
    brush.num_sides = 4
    gennerate_canvas()
    
elif num_ch == 2:
    brush.num_sides = 5
    gennerate_canvas()
    
print("Canvas Gennerated !")

turtle.done()