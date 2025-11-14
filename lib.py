import turtle
import random

class Brush:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
    
    def draw(self) -> None:
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()
        
    def draw_inside(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()
        
        for i in range(0, 2):
            reduction_ratio = 0.618
            turtle.forward(self.size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(self.size*(1-reduction_ratio)/2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            self.size *= reduction_ratio
            self.draw()
            
    def setup(self, speed=int, bg=str, tracer=int, colormode=int) -> None:
        turtle.speed(speed)
        turtle.bgcolor(bg)
        turtle.tracer(tracer)
        turtle.colormode(colormode)
        
class Painter:
    def __init__(self):
        return None
    
    def painter_choice(self):
        while True:
            try:
                in_ = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
                if in_ > 9 and in_ < 1:
                    print("Invalid input. Please enter a number between 1-9")
                return in_
            except ValueError:
                print("Invalid input. Please enter a number between 1-9")

    def drawing_prep(self):
        num_sides = self.random_shape()
        size = self.random_size()
        orientation = self.random_orientation()
        location = self.random_loc()
        color = self.get_new_color()
        border_size = self.random_border()
        return num_sides, size, orientation, location, color, border_size
    
    def random_shape(self):
        return random.randint(3, 5) # triangle, square, or pentagon
        
    def random_size(self):
        return random.randint(50, 150)
    
    def random_orientation(self):
        return random.randint(0, 90)
        
    def random_loc(self):
        return [random.randint(-200, 200), random.randint(-200, 200)]
    
    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def random_border(self):
        return random.randint(1, 10)