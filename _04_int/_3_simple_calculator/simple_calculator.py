"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw

    num1 = simpledialog.askinteger(title='1', prompt='give me a number.')
    num2 = simpledialog.askinteger(title='2', prompt='give me another number.')

    asmd = simpledialog.askstring(title='asmd', prompt='Would you like to add, subtract, multiply, or divide?')

    if asmd == 'add':
        messagebox.showinfo(message=num1+num2)
    elif asmd == 'subtract':
        messagebox.showinfo(message=num1-num2)
    elif asmd == 'multiply':
        messagebox.showinfo(message=num1*num2)
    elif asmd == 'divide':
        messagebox.showinfo(message=num1/num2)
