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
    if num_ch in [1, 2, 3]:
        for i in range(random.randint(25, 35)):
            brush.draw()
            s, o, l, c, b = painter.gennerate_solcb()
            brush.size = s
            brush.orientation = o
            brush.location = l
            brush.color = c
            brush.border_size = b
    elif num_ch == 4:
        for i in range(random.randint(25, 35)):
            brush.draw()
            s, o, l, c, b = painter.gennerate_solcb()
            brush.num_sides = painter.random_shape()
            brush.size = s
            brush.orientation = o
            brush.location = l
            brush.color = c
            brush.border_size = b
    elif num_ch in [5, 6, 7]:
        for i in range(random.randint(25, 35)):
            brush.draw_inside()
            s, o, l, c, b = painter.gennerate_solcb()
            brush.size = s
            brush.orientation = o
            brush.location = l
            brush.color = c
            brush.border_size = b
        
    # elif num_ch == 8:
        
        
    # elif num_ch == 9:

print("Gennerating Canvas . . .")

if num_ch == 1:
    brush.num_sides = 3
    gennerate_canvas()
    
elif num_ch == 2:
    brush.num_sides = 4
    gennerate_canvas()
    
elif num_ch == 3:
    brush.num_sides = 5
    gennerate_canvas()
    
elif num_ch == 4:
    gennerate_canvas()
    
elif num_ch == 5:
    brush.num_sides = 3
    gennerate_canvas()
    
elif num_ch == 6:
    brush.num_sides = 4
    gennerate_canvas()
    
elif num_ch == 7:
    brush.num_sides = 7
    gennerate_canvas()
    
# eli
    
print("Canvas Gennerated !")

turtle.done()