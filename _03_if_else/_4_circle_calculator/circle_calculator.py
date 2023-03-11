# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

import math
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw

    radius = simpledialog.askinteger(title='circle', prompt='What is the radius of a circle?')

    circle = simpledialog.askstring(title='circle', prompt='Do you want to calculate the area or circumference of a circle?')

    area = math.pi*radius*radius
    circumference = 2*math.pi*radius

    if circle == 'area':
        messagebox.showinfo(message=area)
    elif circle == 'circumference':
        messagebox.showinfo(message=circumference)
#Area = πr^2
#Circumference = 2πr 