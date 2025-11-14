import turtle
import random

class Painter:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
    
    def draw_polygon(self) -> None:
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

    def setup(self, speed=int, bg=str, tracer=int, colormode=int) -> None:
        turtle.speed(speed)
        turtle.bgcolor(bg)
        turtle.tracer(tracer)
        turtle.colormode(colormode)
        
class User:
    def __init__(self):
        return None
    
    def user_choice(self):
        while True:
            try:
                in_ = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
                if in_ > 9 and in_ < 1:
                    print("Invalid input. Please enter a number between 1-9")
                return in_
            except ValueError:
                print("Invalid input. Please enter a number between 1-9")

    def drawing_prep(self):
        num_sides = random.randint(3, 5) # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-200, 200), random.randint(-200, 200)]
        color = self.get_new_color()
        border_size = random.randint(1, 10)
        return num_sides, size, orientation, location, color, border_size
    
    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))