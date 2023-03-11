from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    pizza = 'y u m'
    water = 'e'
    cat = 'a'
    dog = 'b'
    fish = 'c'
    parrot = 'd'

    input = simpledialog.askstring(title='t', prompt='f')

    if input == 'pizza':
        messagebox.showinfo(message=pizza)
    elif input == 'water':
        messagebox.showinfo(message=water)
    elif input == 'cat':
        messagebox.showinfo(message=cat)
    elif input == 'dog':
        messagebox.showinfo(message=dog)
    elif input == 'fish':
        messagebox.showinfo(message=fish)
    elif input == 'parrot':
        messagebox.showinfo(message=parrot)