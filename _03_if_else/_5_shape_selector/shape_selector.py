import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    my_turtle = turtle.Turtle()

    shape = simpledialog.askstring(title='shape selector', prompt='What shape do you want to draw?')

    if shape == 'triangle':
        for i in range(3):
            my_turtle.forward(100)
            my_turtle.right(360/3)
    elif shape == 'square':
        for i in range(4):
            my_turtle.forward(100)
            my_turtle.right(360/4)
    elif shape == 'circle':
        for i in range(100):
            my_turtle.forward(8)
            my_turtle.right(360/100)
    else:
        for i in range(8):
            my_turtle.forward(100)
            my_turtle.right(360/8)
    # Make a new turtle
    
    # Ask the user what shape they want to draw and store it in a variable
    
    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
